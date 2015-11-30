Instrukcja instalacji
===========================

Baza danych: Postgresql.


Instrukcja postawienia bazy danych
-------------------------

Logowanie do postgres'a:
`sudo -i`
`su postgres`
`cd`

Pobieranie skryptu dla debiana:
wget https://docs.djangoproject.com/en/dev/_downloads/create_template_postgis-debian.sh

Uruchamianie skryptu:
`chmod 755 ./create_template_postgis-debian.sh`
``./create_template_postgis-debian.sh`

Tworzenie bazy danych:
`createdb -T template_postgis NAZWA_BAZY_DANYCH`

Ustawianie hasła dla user'a postgres:
`psql NAZWA_BAZY_DANYCH`
``\password postgres`




Instrukcja konfiguracji projektu
-------------------------


1. Skopiuj settings-example.py i nazwij go settings.py zapisując w tym samym katalogu.
2. W settings.py ustaw dane do swojej bazy danych.
3. Wykonaj polecenia (tylko raz, przy konfiguracji):
`python manage.py syncdb`
`python manage.py makemigrations`
`python manage.py migrate`

Uruchomienie serwera
-------------------------

`python manage.py runserver`
