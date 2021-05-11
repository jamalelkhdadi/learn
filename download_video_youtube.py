# pip install pytube
# pip install git+https://github.com/pytube/pytube


from pytube import YouTube
from pytube import Playlist


link = ""

video = YouTube(link)

# print(f"title {video.title}")
# print(f"title {video.description}")
# print(f"title {video.views}")
# print(f"title {video.rating}")
# print(f"title {video.length}")

# for stream in video.streams.filter(progressive=True, res="720p"):
#    print(stream)


def finish():
    print("Download done")


video.streams.get_highest_resolution().download(
    output_path="/home/user/Downloads")
video.register_on_complete_callback(finish())

##########################################################

# playlist

playlist_link = ""

playlist = Playlist(playlist_link)

for video in playlist.videos:
    video.streams.get_highest_resolution().download(
        output_path="/home/user/Downloads")
    video.register_on_complete_callback(finish())
