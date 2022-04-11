##10-3

filepath = "files/guestbook.txt"

with open(filepath, 'a') as txt_file:
    while True:
        name = input('What is your name: ')

        if name == 'quit':
            quit()
        else:
            print("Hello " + name + ", Welcome!" )
            txt_file.write("My name is " + name + "\n")



