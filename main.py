# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

movie_list = ['Star Wars: Episode IV – A New Hope', 'Jaws', 'Empire of the Sun', 'A.I. Artificial Intelligence', 'War Horse']


toto_albums = ['Fahrenheit','The Seventh One','Toto XX','Falling in Between','35th Anniversary – Live in Poland','Toto XIV','Old Is New','Tours Around the Sun - Live in Holland']


def alphabetical_order(movies):
    alphabetical = movies.sort()
    return alphabetical

def won_golden_globe(x):
    won_list = ['Jaws', 'Star Wars: Episode IV – A New Hope', 'E.T. the Extra-Terrestrial', 'Memoirs of a Geisha']
    x = x.lower()
    for i in range(len(won_list)):
        won_list[i] = won_list[i].lower()
    won = x in won_list
    if won == True:
        return(f'{x} has won a Golden Globe')
    else:
        return(f'{x} did not win a Golden Globe')
        
   

def remove_toto_albums(x):
    if toto_albums[0] in movie_list:
        x.remove(toto_albums[0]) 
    if toto_albums[1] in movie_list:
        x.remove(toto_albums[1])
    if toto_albums[2] in movie_list:
        x.remove(toto_albums[2])
    if toto_albums[3] in movie_list:
        x.remove(toto_albums[3])
    if toto_albums[4] in movie_list:
        x.remove(toto_albums[4])
    if toto_albums[5] in movie_list:
        x.remove(toto_albums[5])

alphabetical_order(movie_list)

print(movie_list)
print(won_golden_globe(movie_list[1]))
print(won_golden_globe(movie_list[2]))
remove_toto_albums(movie_list)


