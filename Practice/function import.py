from functions import make_album

while True:
    print('enter quit to quit anytime')
    artist = input("What is the name of the artist: ")
    album = input("What is the name of album? ")
    number = input("How many songs fella?")

    hehe = make_album(artist,album,number)
    for key, value in hehe.items():
        print(key + " : " + value)

