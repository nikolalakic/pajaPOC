import random

import pandas as pd

df = pd.read_excel('Filmovi_serije.xlsx')
filmovi = df['Filmovi'].to_list()
filmovi_imdb = df['Film_imdb'].to_list()

film = random.choice(filmovi)
filmovi_imdb_index = filmovi.index(film)
link = filmovi_imdb[filmovi_imdb_index]

print(f'\nNasumicni film je: ', film)
print(f'IMDB link za nasumicni film je: ', link)


