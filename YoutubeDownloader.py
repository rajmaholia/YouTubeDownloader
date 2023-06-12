from pytube import YouTube
from Video import Video
from pytube.contrib.playlist import Playlist
from pytube.contrib.channel import Channel
import os
import time

class YoutubeDownloader():
  """ Downloads Youtube videos and playlists """
  
  base_dir = "/sdcard/YtDownloads/"
  
  def __init__(self,url,to):
    self.url = url
    self.to = to
    
  
  def add_playlist(self,url):
    """Add playlist url in queue to be downloaded"""
    self.playlists.append(url)
  
  def add_video(self,url):
    """Add videos in queue to be downloaded"""
    self.videos.append(url)
    
  
  def download(self):
    """Handles complete download process ."""
    url_type = self.check_url(self.url)
    if url_type[0] == True and url_type[1] == "VIDEO":
      video = Video(self.url,self.base_dir)
      video.download()
    elif url_type[0] == True and url_type[1] == "PLAYLIST":
      self.download_playlist(self.url)
    else:
      print("Not a valid url")
  
  def download_playlist(self,url):
    """Downloads playlist in queue """
    playlist = Playlist(url)
    channel = Channel(playlist.owner_url)
    channel_name = channel.channel_name
    
    print("\rLoading playlist ...",end=" ")
    
    title = playlist.title
    first_20 =  title[:20] if len(title)>45 else title
    last_20  = f".....{title[-20:]}" if len(title)>45 else " "
    
    
    print(f"\rTitle : {first_20}{last_20} ")
    print(f"No of Videos : {playlist.length}")
    
    for index,url in enumerate(playlist.video_urls):
      print(f"\n(Video {index+1} of {playlist.length})")
      save_to = os.path.join(self.base_dir, self.slugify(channel_name),self.slugify(title))
      video = Video(url,save_to)
      video.download()
      
  def check_url(self,url):
    """Checks url is a playlist or video"""
    try:
        playlist = Playlist(url)
        playlist.playlist_id
        return True,"PLAYLIST"
        
    except:
        try:
            video = YouTube(url)
            return True,"VIDEO"
        except:
            return False,None
  
  def slugify(self,filename):
    """Creates a valid slug from file amd folder names"""
    invalid_chars = "|\'\\?*&<\";:>+[]=/"
    for char in invalid_chars:
      filename =  filename.replace(char,"_")
    return filename
