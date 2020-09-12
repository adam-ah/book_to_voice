# Book to Voice

Convert any long text, science papers or even books,  into speech (mp3).

The project relies on Google TTS, so make sure to sign up and [enable Google TTS on your cloud dashboard](https://cloud.google.com/text-to-speech/docs/quickstart-protocol).

# Step 1 - add TTS credentials

Once you downloaded the token from the Google TTS project, put it in the directory and export it so the project can use it

    export GOOGLE_APPLICATION_CREDENTIALS=`pwd`/TTSproject-0145adae2f93.json


# Step 2 (optional) - Summarise, if too long

The text might be took long so you can create an automatic summary of it by running 

    ./text_summary.py long_text.txt

This will create a ```long_text_summary.txt``` file.

# Step 3 - Convert text to speech

Run 

    ./tts_sample.py long_text.txt

Which will create several mp3 files, starting with ```long_text_000.mp3```.

# Step 4 (optional) - concatenate and tag the MP3

Concatenation is simple, ```cat``` works:

    cat *.mp3 > long_text.mp3

To tag the file, use id3lib (e.g., from brew ```brew install id3lib```)

    id3tag -A "Album name for my full book" long_text.mp3