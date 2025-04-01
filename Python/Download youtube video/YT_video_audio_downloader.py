# First install the imported libraries
# You have to install the ffmpeg(to download only audio) and set the path to ffmpeg.exe 
#    (i.e something like:- C:\\ffmpeg\\bin\\ffmpeg.exe) in the 
#    environment variable or just paste it here

from pytube import YouTube
import sys, os
from pydub import AudioSegment
class YtVideo():
    def __init__(self, url):
        try:
            self.yt = YouTube(url)
        except:
            print("Network error")
            sys.exit()
        self.stream = self.yt.streams
        self.title =""
        self.path = os.environ.get("DOWNLOAD_PATH") # set path where you want to download all your content
        print(self.path)
    def getDetails(self):
        self.title = self.yt.title
        print(f"Title: {self.title}")

    def getResolutions(self):
        resolutions = list(set([stream.resolution for stream in self.stream.filter(progressive=True) if stream.resolution]))
        print(*resolutions)
    
    def downloadVideo(self, res):
        videoStreams = self.stream.filter(progressive=True, res = res, file_extension="mp4")
        videoStream = videoStreams.first()
        print(f"Size: {int(videoStream.filesize)//1024**2} MB" )
        proceed = input("Proceed(Y/N): ")
        if proceed.upper() != 'Y':
            print("Exiting")
            sys.exit()

        p = videoStream.download(output_path= self.path)
        print(f"Downloaded at: {p}")
    
    def downloadAudio(self):
        hasAudio = any(stream.type.startswith("audio") for stream in self.stream  )
        audioStream = self.stream.filter(only_audio=True).first()
        audioStream.download(output_path=self.path)
        self.convertMP4toMP3(os.path.join(self.path,audioStream.default_filename))
        
   
    def convertMP4toMP3(self, mp4File):
        AudioSegment.ffmpeg = os.environ.get("FFMPEG") # your path to ffmpeg
        mp3 = AudioSegment.from_file(mp4File, format="mp4")
        mp3_path = mp4File.replace(".mp4", ".mp3")
        mp3.export(mp3_path, format = "mp3")
        try:
            os.remove(mp4File)
        except FileNotFoundError:
            print("file not found")
        print(f"Audio at {mp3_path}")
      
video = YtVideo(input("Enter video link: "))

video.getDetails()
print("1. video and audio\n2. only audio")
ch = int(input("Enter your choice: "))
if ch==1:
    video.getResolutions()
    res = input("Enter resolution: ")
    video.downloadVideo(res)
elif ch==2:
    video.downloadAudio()
else:
    print("enter valid choice")
    sys.exit()



