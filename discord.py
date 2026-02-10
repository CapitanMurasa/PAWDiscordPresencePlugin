import PAW_python as paw
from pypresence import Presence
import time

player = paw.PAW()
player.setInfo("Discord PAW plugin")

try:
    drp = Presence("1470437029253873861")
    drp.connect()
    print("Discord Connected")
except Exception as e:
    print(f"Discord failed: {e}")

def update():
    try:
        if player.IsPlaybackActive():
            drp.update(
                details = "Playing: " + player.GetTitle(),
                state = "By: " + player.GetArtist(),
                large_image = "play",
                large_text = "Playing on PerfectAudioWorks",
                small_image = "icon_256",
                small_text = "PerfectAudioWorks"
            )
        else:
            drp.clear()
            
    except Exception as e:
        print(f"RPC Error: {e}")


player.register_update(update, 5000)

print("Discord Plugin Registered Successfully")