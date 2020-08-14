import sys
import youtube

def handle_query(query):
    print("[*] Query results: " + query)
    if query=='goodbye':
        sys.exit(0)
    elif query=='player stop':
        youtube.player_stop()
    elif query=='increase volume':
        youtube.player_volume_up()
    elif query=='decrease volume':
        youtube.player_volume_down()
    else:
        youtube.player_stop()
        youtube.vlc_play(query)

    