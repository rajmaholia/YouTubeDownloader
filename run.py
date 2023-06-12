from YoutubeDownloader import YoutubeDownloader

#https://youtube.com/shorts/EvV86bizQlY?feature=share

def run():
  print("\t\t !! Welcome to YoutubeDownloader !!")
  url = input("Enter Url : ")
  print()
  yd = YoutubeDownloader(url,to="/sdcard/YtDownloads/");
  yd.download()
  
if __name__=="__main__":
  run()