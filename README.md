Instrukcja instalacji
===========================

Baza danych: Postgresql.


Instrukcja postawienia bazy danych
-------------------------

Niedługo.


Instrukcja konfiguracji projektu
-------------------------


1. Skopiuj settings-example.py i nazwij go settings.py zapisując w tym samym katalogu.
2. W settings.py ustaw dane do swojej bazy danych.
3. Wykonaj polecenia (tylko raz, przy konfiguracji):
`python manage.py syncdb
python manage.py makemigrations
python manage.py migrate`

Uruchomienie serwera
-------------------------

`python manage.py runserver`
