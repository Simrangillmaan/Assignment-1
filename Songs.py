""" Songs program by Richa Sharma"""


def load(songs):
    i = 0
    not_completed = 0
    while i < len(songs):
        if songs[i][3] == "N":
            print("{:1}. {:40} - {:6} ({})".format(i + 1, songs[i][0], songs[i][1], songs[i][2]) + " N")
            not_completed = not_completed + 1
        else:
            print("{:1}. {:40} - {:6} ({})".format(i + 1, songs[i][0], songs[i][1], songs[i][2]) + " Y")
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
    songs[songs_completed][3] = 'y'
    print("{} from {} Completed".format(songs[songs_completed][0], songs[songs_completed][1]))
    return songs


def append_Songs():


def main_Menu():



def main():
    file_input = open("songs.csv", "r")
    read_data = file_input.readlines()
    songs = []
    for n in read_data:
        values = n.strip().split(',')
        songs.append(values)
    for i in range(len(songs)):
        songs[i][1] = int(songs[i][1])
    songs.sort()
    file_input.close()
    songs_at_start = len(songs)
    print("""
Songs To Learn 1.0 - by Richa Sharma 
{} songs loaded
Menu:
L - List songs
A - Add new Songs
W - Complete a Song
Q - Quit    
    """.format(songs_at_start))
    user_input = input().upper()
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


