def cap_song_repetition(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    '''
    while playlist.count(song) > 3:
        playlist.remove(song)

    return playlist
