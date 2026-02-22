import PAW_python as paw
import time, sys, os

script_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(script_dir, "libs"))

from pypresence import Presence

player = paw.PAW()
player.setInfo("Discord PAW plugin")

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
        player.SendMessageBox(f"RPC Error: {e}")

try:
    drp = Presence("1470437029253873861")
    drp.connect()
    player.SendMessageBox("Discord Connected")
except Exception as e:
    player.SendMessageBox(f"Discord failed: {e}")
else:
    player.register_update(update, 5000)



