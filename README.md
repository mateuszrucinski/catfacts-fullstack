# catfacts-fullstack


Backend:
-------
Po zainstalowaniu pythona tworzymy swój własny folder gdzie będzie backend pythona.
W folderze instalujemy maszynę env:
  python -m venv env

Uruchamiamy naszynę env:
  source ./env/bin/activate

Sprawdzamy czy pokazuje dobra sciezke:
  which pip

Instalujemy lub updatujemy pip:
  python -m pip install --upgrade pip

Tworzymy plik requirements.txt lub dodajemy z projektu catfacts-fullstack

Potem zapisujemy plik i odpalamy komede:
  pip install -r requirements.txt

To nam pobierze zależności bibliotek do naszego lokalnego projektu

Odpalamy aplikację poprzez:
  uvicorn main:app --reload

Gdzie main to nazwa klasy, gdzie mamy napisany nasz backend
