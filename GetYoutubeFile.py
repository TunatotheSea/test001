from moviepy.video.VideoClip import VideoClip
from pytube import Playlist, YouTube
import os
import glob


class GetYoutubePlaylistData:
    def __init__(self, url) -> None:
        self.ytP = Playlist(url)
        self.INIT()

    def INIT(self):
        self.streamsList = []
        for video in self.ytP.videos:
            self.streamsList.append(GetYoutubedata(streams=video.streams))

    def DownloadPlaylist_BestResVideo(self, downloadGroupName = ""):
        '''
        "목록의 영상들을 가장 좋은 화질로 다운받습니다."
        '''
        for i in range(len(self.streamsList)):
            if (downloadGroupName == ""):
                self.streamsList[i].DownloadBestResVideo()
            else:
                downloadName = downloadGroupName + str(i+1)
                self.streamsList[i].DownloadBestResVideo(downloadName = downloadName)

    def DownloadPlaylist_BestabrAudio(self, downloadGroupName = ""):
        '''
        "목록의 영상들의 *소리만을* 가장 좋은 음질로 다운받습니다."
        '''
        for i in range(len(self.streamsList)):
            if (downloadGroupName == ""):
                self.streamsList[i].DownloadBestabrAudio()
            else:
                downloadName = downloadGroupName + str(i+1)
                self.streamsList[i].DownloadBestabrAudio(downloadName = downloadName)

    


class GetYoutubedata:
    def __init__(self, streams = None, url = ""):
        if url != "":
            self.yt = YouTube(url)
            self.streams = self.yt.streams
        else:
            self.streams = streams
        self.videoStreams = self.streams.filter(progressive=True).order_by("resolution")
        self.audioStreams = self.streams.filter(only_audio=True).order_by("abr")

    def DownloadBestResVideo(self, downloadName = ""):
        '''
        "지정된 url의 영상을 가장 좋은 화질로 다운받습니다."
        '''
        filename = self.GetBestResVideo().download()
        print(f"{downloadName} : video downloaded success")
        
        extension = filename.split(".")[-1]
        if downloadName == "":
            return
        files = glob.glob("*." + extension)
        for x in files:
            if x == filename.split("\\")[-1]:
                targetName = [downloadName]
                try:
                    os.rename(x, targetName[0] + '.mp4')
                except:
                    print("none")
    

    def DownloadBestabrAudio(self, downloadName = ""):
        '''
        "지정된 url의 영상의 *소리만을* 가장 좋은 음질로 다운받습니다."
        '''
        filename = self.GetBestabrAudio().download()
        extension = filename.split(".")[-1]
        files = glob.glob("*." + extension)
        for x in files:
            if x == filename.split("\\")[-1]:
                if (downloadName == ""):
                    targetName = os.path.splitext(x)
                else:
                    targetName = [downloadName]
                try:
                    os.rename(x, targetName[0] + '.mp3')
                except:
                    print("none")

    def combine_mp3andmp4(self, mp3, mp4) -> VideoClip:
        import moviepy.editor as mpe
        clip = mpe.VideoFileClip(mp4)
        audio = mpe.AudioFileClip(mp3)
        final = clip.set_audio(audio)
        return final
    

    def GetBestResVideo(self):
        return self.videoStreams.last()

    def GetBestabrAudio(self):
        return self.audioStreams.last()

    # TO Show Data
    def GetStreamsDataAll(self):
        for i, stream in enumerate(self.streams.all()):
            print(f"{i} : {stream}")

    def GetStreamsDataOnlyHighQuality(self):
        for i, stream in enumerate(self.streams.filter(adaptive=True)):
            print(f"{i} : {stream}")

    def GetVideoDataAll(self):
        for i, stream in enumerate(self.videoStreams.all()):
            print(f"{i} : {stream}")

    def GetAudioDataAll(self):
        for i, stream in enumerate(self.audioStreams.all()):
            print(f"{i} : {stream}")

    def ToString(self):
        print("영상 제목 : ", self.yt.title)
        print("영상 길이 : ", self.yt.length)
        print("영상 평점 : ", self.yt.rating)
        print("영상 썸네일 링크 : ", self.yt.thumbnail_url)
        print("영상 조회수 : ", self.yt.views)
        print("영상 설명 : ", self.yt.description)