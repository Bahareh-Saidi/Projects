import yt_dlp
import os

def download_video(url, save_path):
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    url = input("Enter YouTube URL: ").strip()
    save_path = input("Enter folder to save (leave blank for current folder): ").strip()
    if save_path == "":
        save_path = os.getcwd()
    download_video(url, save_path)
    print("Download complete!")

if __name__ == "__main__":
    main()
