from pytube import YouTube

def download_video(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
   
    try:
        youtubeObject.download()

    except:
        print("Error")
    print("Download is completed successfully")

def download_audio(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
   
    try:
        youtubeObject.download()

    except:
        print("Error")
    print("Download is completed successfully")


def main():
    link = input("Enter the YouTube link: ")
    choose = input("Enter v for video / a for audio: ")

    if choose == "v":
        download_video(link)

    elif choose == "a":
        download_audio(link)

if __name__ == "__main__":
    main()
