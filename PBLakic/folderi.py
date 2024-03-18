import os


class KreiranjeFoldera:
    def __init__(self) -> None:
        self.ime_novog_foldera = str(input('Unesi ime novog radnog foldera: '))
        self.korisnik = str(os.getlogin())

    def pocetna_putanja(self):
        if self.korisnik == 'nikolal':
            putanja = "A:/"
        else:
            putanja = f"c:/Users/{self.korisnik}/Documents/"
        return putanja

    def kreiranjefoldera(self):
        global parent
        pocetna_putanja = self.pocetna_putanja()
        lista_foldera = ['/Od_Arhitekte', '/Od_Arhitekte/Dokumentacija', '/Tower', '/Osnove', '/Dokumentacija',
                         '/Dokumentacija/PGD', '/Dokumentacija/PZI']
        if 'ZaPripremu' not in os.listdir(pocetna_putanja):
            os.mkdir(pocetna_putanja + 'ZaPripremu')
            os.mkdir(pocetna_putanja + 'ZaPripremu' + f'/{self.ime_novog_foldera}')
            parent = pocetna_putanja + 'ZaPripremu' + f'/{self.ime_novog_foldera}'
        else:
            if self.ime_novog_foldera in os.listdir(pocetna_putanja + 'ZaPripremu'):
                print(f'Folder {self.ime_novog_foldera} vec postoji.')
            else:
                os.mkdir(pocetna_putanja + 'ZaPripremu' + f'/{self.ime_novog_foldera}')
                parent = pocetna_putanja + 'ZaPripremu' + f'/{self.ime_novog_foldera}'
        for i in lista_foldera:
            os.mkdir(parent + i)
        return parent

    def skidanje(self):
        folder = self.kreiranjefoldera()
        os.chdir(folder + '/Osnove')
        os.system('wget https://github.com/nikolalakic/pajaPOC/blob/master/PBLakic/Za_download/DWG_Fajlovi.7z')

def main():
    klasa = KreiranjeFoldera()
    klasa.skidanje()


if __name__ == "__main__":
    main()
