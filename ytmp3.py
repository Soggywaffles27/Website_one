 
#https://www.youtube.com/watch?v=dQw4w9WgXcQ
def mp3():
  import os
  import subprocess

  import pytube

  yt = pytube.YouTube("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

  vids= yt.streams.all()
  #for i in range(len(vids)):
      #print(i,'. ',vids[i])

  vnum = int(0)

  parent_dir = r"C:\YTDownloads"
  vids[vnum].download(parent_dir)

  new_filename = "newfile"

