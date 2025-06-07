import os

# Detect PSP version and using TV
psp_model = os.getenv("PSP_MODEL", "1000").strip()
tv_out = os.getenv("TV_OUT", "false").lower() == "true"

# Default settings for each version of PSP
default_profiles = {
    "1000": {
        "resolution": "368x208",
        "crf": "25",
        "bitrate_video": "768k",
        "bitrate_audio": "128k",
    },
    "2000": {
        "resolution": "480x272",
        "crf": "23",
        "bitrate_video": "1500k",
        "bitrate_audio": "128k",
    },
    "3000": {
        "resolution": "480x272",
        "crf": "21",
        "bitrate_video": "1500k",
        "bitrate_audio": "128k",
    },
}

# Get default profile for PSP version
profile = default_profiles.get(psp_model, default_profiles["1000"])

# If we need TV output, then change resolution
if tv_out and psp_model in ["2000", "3000"]:
    profile["resolution"] = "720x480"

# Resolution of output video
resolution = os.getenv("PSP_RESOLUTION", profile["resolution"])
# Constant Rate Factor
crf = os.getenv("PSP_CRF", profile["crf"])
# Video bitrate
bitrate_video = os.getenv("PSP_VIDEO_BITRATE", profile["bitrate_video"])
# Audio bitrate
bitrate_audio = os.getenv("PSP_AUDIO_BITRATE", profile["bitrate_audio"])
# Audio frequency
hertz_audio = int(os.getenv("PSP_AUDIO_HZ", 48000))
# In what second of video get image to thumbnail
thumbnail_seconds = int(os.getenv("PSP_THUMBNAIL_SECOND", 1))
