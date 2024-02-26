from pytube import YouTube

def download_media(link, download_type):
    youtubeObject = YouTube(link)

    if download_type == 'v':
        youtubeObject = youtubeObject.streams.get_highest_resolution()

    elif download_type == 'a':
        youtubeObject = youtubeObject.streams.filter(only_audio=True).first()

    try:
        youtubeObject.download()
        print("Download is completed successfully")

    except Exception as e:
        print("Error:", e)



def main():
    link = input("Enter the YouTube link: ")
    choose = input("Enter v for video / a for audio: ").lower()

    if choose == "v":
        download_media(link, 'v')
    elif choose == "a":
        download_media(link, 'a')
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
