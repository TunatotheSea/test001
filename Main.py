if __name__ == "__main__":
    goingOn = True
    while goingOn:
        OneorMulti = input("영상 한 개를 다운받으시려면 One을, 재생목록을 다운받으시려면 Multi를 입력해주세요. (One/Multi) : ")
        if OneorMulti == "One":
            url = input("다운로드 받으실 영상의 주소(url)를 입력하세요. : ")
            from GetYoutubeFile import GetYoutubedata
            converter = GetYoutubedata(url=url)
            print("영상 정보 확인 완료.")

            # Video downloading 
            VorA = input("영상(mp4)를 다운받으시려면 V를, 음원(mp3)만을 다운받으시려면 A를 입력해주세요. (V/A) : ")
            downloadName = input("다운하시려는 파일의 이름을 (확장자 없이) 입력해주세요. : ")
            if VorA == "V":
                converter.DownloadBestResVideo(downloadName=downloadName)
                print("다운로드 완료.")
                goingOn = False
            elif VorA == "A":
                converter.DownloadBestabrAudio(downloadName=downloadName)
                print("다운로드 완료")
                goingOn = False
            else:
                print("잘못 입력하셨습니다. 다시 입력해주세요.")

        elif OneorMulti == "Multi":
            print("*** 주의 사항 ***")
            print("재생 목록이 비공개일 경우 다운받으실 수 없습니다.\n")
            url = input("다운로드 받으실 재생 목록의 주소(url)를 입력하세요. : ")
            from GetYoutubeFile import GetYoutubePlaylistData
            converter = GetYoutubePlaylistData(url=url)
            print("영상 정보 확인 완료.")
            # Video downloading 
            VorA = input("영상(mp4)를 다운받으시려면 V를, 음원(mp3)만을 다운받으시려면 A를 입력해주세요. (V/A) : ")
            downloadName = input("다운하시려는 파일들의 공통 이름을 (확장자 없이) 입력해주세요. 개별 파일 이름은 XXX1, XXX2의 형태로 다운로드 됩니다. : ")
            if VorA == "V":
                converter.DownloadPlaylist_BestResVideo(downloadName=downloadName)
                print("다운로드 완료.")
                goingOn = False
            elif VorA == "A":
                converter.DownloadPlaylist_BestabrAudio(downloadGroupName=downloadName)
                print("다운로드 완료")
                goingOn = False
            else:
                print("잘못 입력하셨습니다. 다시 입력해주세요.")

        else:
            print("잘못 입력하셨습니다. 다시 입력해주세요.")
    

