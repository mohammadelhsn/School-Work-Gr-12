# Import the modules

import pyttsx3
import requests

# Initiate the TTS engine

def main():
    engine = pyttsx3.init()

    # Ask the user for the song name and author (optional)

    song_name = input("What song would you like the TTS to sing (feel free to include the author of the song for a more specific result)? ")

    # Make the API request. Get the lyrics, author and song title

    response = requests.get(f"https://some-random-api.ml/lyrics?title={song_name}")
    data = response.json()

    # Check the length of the dictionary to check for no results!

    if (len(data) == 1): print("No result(s) found! Please try a different song!");main();return
    
    lyrics = data["lyrics"].split("\n")
    result_name = data["title"]
    result_author = data["author"]

    # Tell them what song you're playing 🎵

    print(f"▶️ | Now playing: {result_name} by {result_author}")

    # Loop through the lyrics and say them

    for line in lyrics:
        engine.say(line)
        print(line)
        engine.runAndWait()


    save = input("Would you like an MP3 version of the song? (yes, no)")

    if (save == "yes"):
        file_name = input("What would you like to name the file? ")
        engine.save_to_file(lyrics, f"{file_name}.mp3")
        engine.runAndWait()
    if (save == "no"): return
    else: main();return
main()
