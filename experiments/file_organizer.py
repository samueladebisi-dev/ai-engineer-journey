files = ["image.png", "notes.txt", "music.mp3"]

for file in files:
    if file.endswith(".png"):
        print(file, "is an image")
    elif file.endswith(".txt"):
        print(file, "is a text file")
    elif file.endswith(".mp3"):
        print(file, "is an audio file")
