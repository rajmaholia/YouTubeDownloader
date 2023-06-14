from YoutubeDownloader import YoutubeDownloader

#https://youtube.com/shorts/EvV86bizQlY?feature=share

def run():
  print("\t\t !! Welcome to YoutubeDownloader !!")
  url = input("Enter Url : ")
  print()
  try:
    yd = YoutubeDownloader(url,to="/sdcard/YtDownloads/");
    yd.download()
  except Exception as e:
    print(f"Error : {e}")
    
if __name__=="__main__":
  run()