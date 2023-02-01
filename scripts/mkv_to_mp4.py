import os
import ffmpeg

def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = name + ".mp4"
    ffmpeg.input(mkv_file).output(out_name).run()
    print("Finished converting {}".format(mkv_file))

convert_to_mp4("/home/youss-taouil/projects/project_NAS/NAS/static/root/home/youss-taouil/video.mkv")