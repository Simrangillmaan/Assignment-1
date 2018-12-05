""" Songs program by Richa Sharma"""


def load():
    songs_file = open('songs.csv', 'w+')
    songs_data = songs_file.readlines()
    required_details = []
    completed_details = []

    for song_line in songs_data:
        if "r" in song_line:
            data = song_line.strip().split(",")
            required_details.append(data)
        else:
            data = song_line.strip().split(",")
            completed_details.append(data)
    print(required_details)