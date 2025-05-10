class Hotstar:
    def __init__(self,username,pwd):
       self.username=username
       self.__pwd=pwd
       print(f"Hello {self.username}.You have succesfully logged in")
    def content_access(self):
        print("Welcome to Disney hotstar\nlimitted content")
    def ads(self):
        print("Ads................are running")
    def videoqua(self):
        print("video is playing in 720p")
    def livesports(self):
        print("You don't have access to livesports")
    def Download(self):
        print("You don't have access to download the video")
    def logins(self):
        print("You can login in single device")

class  premium:
    def __init__(self,username,pwd):
       self.username=username
       self.__pwd=pwd
       print(f"Hello {self.username}.You have succesfully logged in")
    def content_access(self):
        print("Welcome to Disney hotstar full content")
    def ads(self):
        print("Ads will not run")
    def videoqua(self):
        print("video is playing in 4k")
    def livesports(self):
        print("You  have access to livesports")
    def Download(self):
        print("You  have access to download the video")
    def logins(self):
        print("You can login in multiple device at a time")



teja=Hotstar("Teja","Teja123")
teja.content_access()
teja.ads()
teja.Download()
teja.livesports()
teja.logins()

dinesh=premium("Dinesh","Dinesh123")
dinesh.content_access()
dinesh.ads()
dinesh.Download()
dinesh.livesports()
dinesh.logins()


