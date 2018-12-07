""" Songs program by Richa Sharma"""
def load(songs):

def complete_Song(songs):


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

