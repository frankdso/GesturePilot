import spotipy
from spotipy.oauth2 import SpotifyOAuth

def play_spotify():
    print("[ACTION] Starting Spotify playback...")

    scope = "user-read-playback-state user-modify-playback-state"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="",
        client_secret="",
        redirect_uri="http://127.0.0.1:8888/callback",
        scope=scope
    ))

    # Filter device by name
    my_device_name = "FRANCISDSOUZA"
    devices = sp.devices()
    device_id = None

    for d in devices["devices"]:
        if d["name"] == my_device_name:
            device_id = d["id"]
            break

    if device_id:
        sp.start_playback(
            device_id=device_id,
            context_uri="spotify:playlist:"  # Replace with your own
        )
        print(f"[DEBUG] Playing on device: {my_device_name}")
    else:
        print("[ERROR] Your desktop device 'FRANCISDSOUZA' was not found. Is Spotify open?")
        
def toggle_play_pause(sp):
    print("[ACTION] Toggling Play/Pause...")
    try:
        playback = sp.current_playback()
        if playback and playback["is_playing"]:
            sp.pause_playback()
        else:
            devices = sp.devices()["devices"]
            if devices:
                active_id = devices[0]["id"]
                sp.start_playback(device_id=active_id)
            else:
                print("[ERROR] No active Spotify device found.")
    except Exception as e:
        print(f"[ERROR] Spotify Play/Pause failed: {e}")


def next_song(sp):
    sp.next_track()
    print("[ACTION] Next Track")

