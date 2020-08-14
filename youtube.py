import requests
import re
import subprocess
import threading 
import vlc
import pafy

# youtube watch link init
youtube_url = "https://www.youtube.com/results?search_query="
url_regex = '"/watch\?v=\w*"'

# vlc init
player_is_playing = False
current_player_volume = 70

Instance = vlc.Instance()
player = Instance.media_player_new()
player.audio_set_volume(current_player_volume)

def get_song_url(query):
    query = query.replace(' ','+')
    complete_url = youtube_url + query
    r = requests.get(complete_url)
    doc = r.content
    video_url = re.search(url_regex,doc).group(0)
    return video_url

def vlc_play(query):
    global player_is_playing
    player_is_playing = True
    player_thread = threading.Thread(target=python_vlc, args=(query,))
    player_thread.start()

def player_stop():
    global player_is_playing
    player_is_playing = False
    player.stop()

def change_player_volume(volume):
    player.audio_set_volume(volume)

def player_pause():
    global player_is_playing
    player_is_playing = False
    player.pause()
    
def player_resume():
    global player_is_playing
    if not player_is_playing:
        player_is_playing = True
        player.resume()

def player_volume_up():
    global current_player_volume
    current_player_volume += 10
    change_player_volume(current_player_volume)

def player_volume_down():
    global current_player_volume
    current_player_volume -= 10
    change_player_volume(current_player_volume)

def python_vlc(query):
    song_url = "https://www.youtube.com" + get_song_url(query).strip('"')
    video = pafy.new(song_url)
    best_match = video.getbest()
    play_url = best_match.url

    Media = Instance.media_new(play_url)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
        