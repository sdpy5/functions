def make_album(artist_name,album_name,tracks = ''):
    album = {'artist name':artist_name,'album name':album_name,'tracks':tracks}
    return album




while True:
    art_name = input('enter artist name : ')
    if art_name == 'quit':
        break
    alb_name = input('enter album name : ')
    if alb_name == 'quit':
        break
    trk = int(input('enter the number of tracks : '))
    if trk == 'quit':
        break


    albss = make_album(art_name,alb_name,trk)
    print(albss)