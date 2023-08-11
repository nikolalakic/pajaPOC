# pajaPOC
Pajine potrebe

### Ansible instalacija:
 
 Instaliraj na linux masini odakle kontrolises ostale masine:

 ```python3 -m pip install --user ansible```

 Proveri dal je uspelo sa ```ansible --version```

### 2. Prvo napravi ssh kljuc koji ce da koristi samo Ansible pod nazivom ansible:
```ssh-keygen -t ed25519 -C "Ansible kljuc"```

Default putanja za ssh kljuceve je ```/home/$USER/.ssh/``` napravice se pod nazivom ed25519 privatni i ed25519.pub javni, ti ih preimenuj u ansible i ansible.pub

Kreiraj folder /home/$USER/logincontrol na hostu i targetu jer scp nesto zeza bez toga.

### 3. ansible.cfg

Vidi u trecoj liniji promeni ```$USER``` u svoj nickname ako ne radi, promeni port i ostalo po potrebi

### 4. inventory.yaml

U plejbukovima samo u prvoj liniji zameni naziv "lokalno" ili "sajt" sta ti vec treba, u inventory.yaml ispod hosts linije zameni ip adrese koje ti trebaju, pod kojim nazivom se pokrece playbook te na te ip adrese se kacis

### 5. Alias

Napravi alias u .bash_aliases ili koji vec shell koristis kao:

alias pajapoc='cd <putanja_do_git_foldera> && ansible-playbook <putanja_do_git_foldera>/playbooks/plejbook.yml && cd'

