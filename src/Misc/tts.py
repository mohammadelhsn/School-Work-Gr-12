import pyttsx3
import requests
def main():
    engine = pyttsx3.init()
    song_name = input(
        "What song would you like the TTS to sing (feel free to include the author of the song for a more specific result)? "
    )
    response = requests.get(f"https://some-random-api.ml/lyrics?title={song_name}")
    data = response.json()
    if len(data) == 1:
        print("No result(s) found! Please try a different song!")
        main()
        return
    lyrics = data["lyrics"].split("\n")
    result_name = data["title"]
    result_author = data["author"]
    print(f"▶️ | Now playing: {result_name} by {result_author}")
    for line in lyrics:
        engine.say(line)
        print(line)
        engine.runAndWait()
    save = input("Would you like an MP3 version of the song? (yes, no)")
    if save == "yes":
        file_name = input("What would you like to name the file? ")
        engine.save_to_file(lyrics, f"{file_name}.mp3")
        engine.runAndWait()
    if save == "no":
        return
    else:
        main()
        return
main()
