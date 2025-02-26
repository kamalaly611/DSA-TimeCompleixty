import win32com.client

def pronounce_names(names):
    # Initialize the speech engine
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    
    for name in names:
        # Construct the shoutout message
        shoutout = f"Hey Kamal know I will give shout out to your freinds {name}"
        # Pronounce the shoutout
        speaker.Speak(shoutout)

if __name__ == "__main__":
    names_list = ["Samii", "Khaliid", "Kaamaloo"]
    pronounce_names(names_list)
