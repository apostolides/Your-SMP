import snowboydecoder
import sys
import signal
import assistant
import query_handler as qh
import youtube

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def main_handler():
    youtube.change_player_volume(5)
    snowboydecoder.play_audio_file()
    try:
        query = assistant.recognize_from_mic()
        youtube.change_player_volume(youtube.current_player_volume)
        print('[*] Sending request...')
        qh.handle_query(query)
    except:
        pass
    print('Listening... Press Ctrl+C to exit')

if len(sys.argv) == 1:
    print("Usage: python demo.py your.model")
    sys.exit(-1)

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=main_handler,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
