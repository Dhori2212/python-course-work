from abc import ABC, abstractmethod

# Abstract class
class content(ABC):
    @abstractmethod
    def upload(self):
        pass
# photo class
class photo(content):
    def upload(self):
        print("compressing photo.....")
        print("uploading photo................")
        print("photo uploaded successfully!")
#Video Class
class Video(content):
    def upload(self):
        print("Encoding video......")
        print("uploading video.....")
        print("Video uploaded successfully!")
#Reel Class (New feature added easily)
class  Reel(content):
    def upload(self):
        print("Adding effects to reel...")
        print("uploading reel....")
        print("Reel uploaded successfully!")
#usage
contents = [photo(), Video(), Reel()]
#cont=Photo()
#cont.upload()
for content in contents:
    content.upload()