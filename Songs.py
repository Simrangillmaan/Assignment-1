""" Songs program by Richa Sharma"""


def load(songs):
    i = 0
    not_completed = 0
    while i < len(songs):
        if songs[i][3] == "N":
            print("{:2}.  {:40} - {:8} ({})".format(i + 1, songs[i][0], songs[i][1], songs[i][2]))
            not_completed = not_completed + 1
        else:
            print("{:2}. *{:40} - {:8} ({})".format(i + 1, songs[i][0], songs[i][1], songs[i][2]) )
        i = i + 1
    songs_completed = len(songs) - not_completed
    print("{} Songs learnt, {} Songs to learn ".format(songs_completed, not_completed))


def complete_Song(songs):
    while True:
        try:
            songs_completed = int(input("Enter the number of a song to mark as learned ")) - 1
            if 'y' in songs[songs_completed]:
                print("You have already Learned {} ".format(songs[songs_completed][0]))
                continue
            if songs_completed < 0 or songs_completed > len(songs) - 1:
                print("Not a vaild input")
                continue
            break
        except ValueError:
            print("please enter a number")
    songs[songs_completed][3] = 'Y'
    print("{} from {} Completed".format(songs[songs_completed][0], songs[songs_completed][1]))
    return songs

def main_Menu():
    print(""" Menu:
    L - List Songs
    A - Add a new Songs
    C - Complete a Song
    Q - Quit
        """)
    user_input = input().upper()
    return user_input

def append_Songs():
    new_Song = []
    song_Name = str(input("Title: "))

    while True:
        try:
             song_Year = int(input("Year: "))
             if  song_Year < 0:
                print("Number must be >= 0")
                continue
             break
        except ValueError:
            print("Invalid input; enter a valid number")
    while True:
        try:
            song_Artist = str(input("Artist: "))
            if song_Artist == '' or song_Artist == ' ':
                print("Input can not be blank")
                continue
            if '  ' in song_Artist:
                print("Input contains too many spaces")
            break
        except ValueError:
            print("Input can not be a number")

    new_Song.append(song_Name)
    new_Song.append( song_Artist)
    new_Song.append(song_Year)
    new_Song.append('N')
    print("{} by {} ({}) added to Songs list".format(song_Name, song_Artist, song_Year))
    return new_Song











def main():

    file_input = open("songs.csv", "r")
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




if __name__ == '__main__':
    main()

