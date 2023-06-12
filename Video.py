from pytube import YouTube
import os

class Video(YouTube):
  """ Downloads Youtube vide amd playlists """
  
  
  def __init__(self,url,to):
    super().__init__(url)
    self.to = to
    self.downloaded = False

  def is_available(self):
    """Checks Availability of youtube video"""
    try:
      self.check_availability()
      return True
    except:
      return False
  
    
  def download_tracker_callback(self,chunk,file_handler,remaining_bytes):
    """Shows downloading process of video . """
    bar_width = 40
    total_bytes = chunk.filesize
    downloaded_bytes = total_bytes - remaining_bytes
    downloaded_percent = (downloaded_bytes / total_bytes)*100
    bar_progress  = int((downloaded_bytes / total_bytes)*bar_width)
    progress = f"\r[{'#'*bar_progress}{' '*(bar_width - bar_progress)}] {downloaded_percent:.2f}%"
    print(progress,end=" ")
  
  
  def download_complete_callback(self,stream,file_path):
    """ Defines what to do after video has been downloaded ."""
    print(f"\r[DOWNLOADED] {' '*40}")
  
  
  def choose_stream(self):
    """Returns stream choosem to download . """
    pass
  
  def download_stream(self,stream,to):
    try:
      saved_to = stream.download(to)
      self.downloaded = True
      print(f"Saved to : {saved_to}")
    except:
      self.download_stream(stream,to)
  
  def create_dirs(self):
    """Creates dirs recursively for video's saved location if it doesn't exists"""
    try:
      os.makedirs(self.to)
    except:
      pass 
    
    
  def download(self):
    """Handles complete download process ."""
    self.register_on_progress_callback(self.download_tracker_callback)
    self.register_on_complete_callback(self.download_complete_callback)
    
    print("\rChecking Availability ...   ",end=" ")
    
    if self.is_available():
      print("\rChecking Availability ...  OK",end=" ")
      print("\rSelecting Stream ...          ",end=" ")
      stream = self.streams.filter(res="360p",mime_type="video/mp4")[0]
      stream_title = stream.title
      first_20 =  stream_title[:20] if len(stream_title)>45 else stream_title
      last_20  = f".....{stream_title[-20:]}" if len(stream_title)>45 else " "
      stream_size = (stream.filesize)/(1024*1024)
      print(f"\rTitle : {first_20}{last_20}   Size : {stream_size:.2f}MB")
      print(f"\r[{' '*40}] 0%",end=" ")
      
      self.create_dirs()
      
      self.download_stream(stream,self.to)
      print()
    else:
      print("\rVideo Not Available               ")
  