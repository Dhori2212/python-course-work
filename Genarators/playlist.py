def music(tracks):
   for song in tracks:
      yield song
     
playlist1=["Om Jai Jagdish Hare – Aarti (Hindi)","Hanuman Chalisa – Hariharan (Hindi)","Bhajare Gopalam – M. Balamuralikrishna (Telugu)"

]
playlist2=["Srivalli – Pushpa","Kalavathi – Sarkaru Vaari Paata"]
playlist3=["Tum Hi Ho – Aashiqui 2","Kesariya – Brahmastra"]


print('Welcome to spotifyyyy!!!!!!!!')
print('1.playlist-1\n2.playlist-2\n3.playlist-3')
op=int(input("select the playlist: "))
if op==1:
    s=music(playlist1)
    print(next(s),"playing...................")
    while True:
       sta=int(input("Enter 1 to play next song: "))
       if sta:
          print(next(s),"playing...................")
       else:
          print("Thanks for choosing spotifyyyy")
          break
elif op==2:
   b=music(playlist2)
   print(next(b),"playing...................")
   while True:
       sta=int(input("Enter 1 to play next song: "))
       if sta:
          print(next(b),"playing...................")
       else:
          print("Thanks for choosing spotifyyyy")
          break
elif op==3:
   c=music(playlist3)

   print(next(c),"playing...................")
   while True:
       sta=int(input("Enter 1 to play next song: "))
       if sta:
          print(next(c),"playing...................")
       else:
          
          break