#https://www.youtube.com/watch?v=dQw4w9WgXcQ
def mp3():
  import os
  import subprocess

  import pytube

  yt = pytube.YouTube("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

  vids= yt.streams.all()
  for i in range(len(vids)):
      print(i,'. ',vids[i])

  vnum = int(input("Enter vid num: "))

  parent_dir = r"C:\YTDownloads"
  vids[vnum].download(parent_dir)

  new_filename = input("Enter filename (including extension): "))  # e.g. new_filename.mp3

  default_filename = vids[vnum].default_filename  # get default name using pytube API
  subprocess.run([
      'ffmpeg',
      '-i', os.path.join(parent_dir, default_filename),
      os.path.join(parent_dir, new_filename)
  ])

  print('done')
