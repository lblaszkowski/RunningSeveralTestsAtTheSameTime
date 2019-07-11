# RunningSeveralTestsAtTheSameTime


Mini projekt zawiera - uruchomienie kilku testów jednocześnie.Uruchomienie kilku testów jednocześnie w konsoli 

Projekt zawiera biblioteki:
- py.test
- py.test-xdist

Wpisanie w Konsole:

pytest test_searchMovies_Saw.py -n 1 (Uruchomienie  testów jeden po drugim )

lub

pytest test_searchMovies_Saw.py -n 2 (Uruchomienie testów jednocześnie )

albo

pytest -n 2 (Uruchomienie testów jednocześnie w dwóch różnych przeglądarkach )


