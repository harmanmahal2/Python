#8-3

##def make_shirt(size, text="I love Python"):
    ##print("You are ordering a " + size + " size shirt with " + text + " text")

##make_shirt('large')

#8-7

def make_album(artist, title, songs = None):
    if songs:
        album = {'artist': artist, 'title': title, 'no. of songs': songs}
    else:
        album = {'artist': artist, 'title': title}

    return album

while True:
    print('enter quit to quit anytime')
    artist = input("What is the name of the artist: ")
    album = input("What is the name of album? ")
    number = input("How many songs fella?")

    hehe = make_album(artist,album,number)
    for key, value in hehe.items():
        print(key + " : " + value)