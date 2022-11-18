#https://www.youtube.com/watch?v=dQw4w9WgXcQ
def mp3():
  import youtube_dl
  def download_ytvid_as_mp3():
      video_url = input("enter url of youtube video:")
      video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
      filename = f"{video_info['title']}.mp3"
      options={
          'format':'bestaudio/best',
          'keepvideo':False,
          'outtmpl':filename,
      }

      with youtube_dl.YoutubeDL(options) as ydl:
          ydl.download([video_info['webpage_url']])

      print("Download complete... {}".format(filename))
  download_ytvid_as_mp3()
