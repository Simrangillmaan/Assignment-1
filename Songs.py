""" Songs program by Richa Sharma"""

import csv  #Importing Csv package to use Csv write

def load(songs):
    """Load function to load the songs from the CSV"""
    i = 0
    not_completed = 0
    while i < len(songs):
        if songs[i][3] == "n":
            print("{:2}.  {:40} - {:8} ({})".format(i + 1, songs[i][0], songs[i][1], songs[i][2]))
            not_completed = not_completed + 1 #Counter to count number of songs not completed
        else:
            print("{:2}. *{:40} - {:8} ({})".format(i + 1, songs[i][0], songs[i][1], songs[i][2]) )
        i = i + 1
    songs_completed = len(songs) - not_completed # calculating number of songs completed
    print("{} Songs learnt, {} Songs to learn ".format(songs_completed, not_completed))


def complete_Song(songs):
    """This is function to complete or learn the song, this asks user for the input of song number, this function gives exception like if a song that is already learnt
    is selected again to learn, throws a message showing that you have already learnt this song"""
    while True:
        try:
            songs_completed = int(input("Enter the number of a song to mark as learned ")) - 1
            if 'y' in songs[songs_completed]:
                print("You have already Learned {} ".format(songs[songs_completed][0]))
                continue
            if songs_completed < 0 or songs_completed > len(songs) - 1: #checking if the input is in the range
                print("Not a vaild input")
                continue
            break
        except ValueError:
            print("please enter a number")
    songs[songs_completed][3] = 'y'
    print("{} from {} Completed".format(songs[songs_completed][0], songs[songs_completed][1]))
    return songs

def main_Menu():
    """This is the function to show the menu to the user, user can Enter the choice according to his need,
     this function returns user input"""
    print(""" Menu:
    L - List Songs
    A - Add a new Songs
    C - Complete a Song
    Q - Quit
        """)
    user_input = input().upper() #Getting the choice input from the user and converting it to upper case.
    return user_input

def append_Songs():
    """This function is used for adding new songs to list"""
    new_Song = [] #list to store new song details
    song_Name = str(input("Title: ")) #getting title from the user

    while True:
        #Exception Handling
        try:  #Trying for the exceptions
             song_Year = int(input("Year: "))
             if  song_Year < 0:      #checking if the song year is a negative value
                print("Number must be >= 0")
                continue
             break
        except ValueError:
            print("Invalid input; enter a valid number") # throwing exception if a year is not number
    while True:
        #Exception Handling
        try:
            song_Artist = str(input("Artist: ")) #Getting the detail for Artist from the user
            if song_Artist == '' or song_Artist == ' ': #Checking if the artist name enter is blank
                print("Input can not be blank")
                continue
            if '  ' in song_Artist:  #Checking for blank spaces in artist name
                print("Input contains too many spaces")
            break
        except ValueError: #Throwing Exception if the Artist name is not string but, integer
            print("Input can not be a number")

     #In the below statements we are appending the new_Song list with the values given by the user
    new_Song.append(song_Name)
    new_Song.append( song_Artist)
    new_Song.append(song_Year)
    new_Song.append('n')
    print("{} by {} ({}) added to Songs list".format(song_Name, song_Artist, song_Year))
    return new_Song


def songs_to_Csv(songs,songs_at_start):
    songs_added = len(songs) - songs_at_start
    songs_final = songs_added + songs_at_start
    print("""
            {} Songs saved to Songs.csv
            Have a nice day :)
                """.format(songs_final))
    for i in range(len(songs)):
        songs[i][1] = str(songs[i][1])
    out_file = open("songs.csv", 'w',newline='')
    writer=csv.writer(out_file)
    writer.writerows(songs)
    out_file.close()

def main():

    file_input = open("Songs.csv", "r")
    read_data = file_input.readlines()

    songs = []
    for n in read_data:
        values = n.strip().split(',')
        songs.append(values)

    for i in range(len(songs)):
        songs[i][1] = str(songs[i][1])
    songs.sort()
    file_input.close()
    songs_at_start = len(songs)
    print("""
Songs To Learn 1.0 - by Richa Sharma 
{} songs loaded""".format(songs_at_start))

    user_input= main_Menu()
    while user_input != "Q":

        if user_input == "L":
            load(songs);
            user_input = main_Menu();
        elif user_input == "A":
            songs.append(append_Songs())
            songs.sort()
            user_input = main_Menu();
        elif user_input == "C":
            songs = complete_Song(songs)
            user_input = main_Menu();

        else:
            print("Invalid Input, Please input from the Choice given")
            user_input = main_Menu()

    songs_to_Csv(songs, songs_at_start);


if __name__ == '__main__':
    main()

