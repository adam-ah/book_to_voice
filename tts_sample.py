#!/usr/bin/env python3
"""Synthesizes speech from the input string of text or ssml.
export GOOGLE_APPLICATION_CREDENTIALS=`pwd`/TTSproject-01455da82f9b.json

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
import argparse
import sys

parser = argparse.ArgumentParser(description='Convert text file to MP3')
parser.add_argument('input', metavar='input', type=str, 
                    help='Name of the input .txt file')

args = parser.parse_args()

input_filename = args.input
output_filename = input_filename.replace('.txt', '')

def preprocess(s):
    s = s.replace('- ', '')
    s = s.replace('\t', ' ')
    while '  ' in s:
        s = s.replace('  ', ' ')
    return s

# Instantiates a client
client = texttospeech.TextToSpeechClient()

f = open(input_filename, "r")
input_text = f.read()

input_text = preprocess(input_text)

voice = texttospeech.VoiceSelectionParams(
    language_code="en-US-Wavenet-B", ssml_gender=texttospeech.SsmlVoiceGender.MALE
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

input_text_chunks = input_text.split('\n')

text = ''

def to_mp3(text, section):
    print(f"Text size is {len(text)}")
    synthesis_input = texttospeech.SynthesisInput(text=text)

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(f"{output_filename}_{section:03}.mp3", "wb") as out:
        out.write(response.audio_content)
        print(f"Section {section} done")

section = 1

for i in range(len(input_text_chunks)):
    chunk = input_text_chunks[i]

    if len(text) + len(chunk) < 5000:
        text += ' ' + chunk
        continue

    to_mp3(text, section)
    section += 1
    text = ''

to_mp3(text, section)
