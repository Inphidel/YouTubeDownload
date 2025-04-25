import yt_dlp

# Prompt user for URL
video_url = input("Please enter the YouTube video URL: ")
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print("Download completed successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
