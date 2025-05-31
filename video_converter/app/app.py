from values import *
import os


def convert_video(inp):
    input_path = f"input_videos/{inp}"
    output_path = f"output_videos/{''.join(inp.split('.')[:-1]) + '.mp4'}"
    out = os.popen(f"""
ffmpeg -i "{input_path}" \
-c:v libx264 -s {resolution} -crf {crf} \
-x264-params me=-x264-params:me=rc-lookahead=10:bframes=16:b-pyramid=none:weightp=0:me=umh:subme=11:8x8dct=0 \
-c:a aac -b:a {bitrate_audio} -ar {hertz_audio} -ac 2 \
-f psp -strict -2 \
"{output_path}"
""")
    print(out.read())

def make_thumbnail(inp):
    input_path = f"input_videos/{inp}"
    output_path = f"output_videos/{''.join(inp.split('.')[:-1]) + '.thm'}"
    out = os.popen(f"""
ffmpeg -i "{input_path}" -f image2 -ss 1 -frames 1 -s 160x120 "{output_path}"
""")
    print(out.read())

if __name__ == "__main__":
    all_videos = os.listdir("input_videos")
    for video in all_videos:
        convert_video(video)
        make_thumbnail(video)

    print(all_videos)
    # convert_video(inp_vid)