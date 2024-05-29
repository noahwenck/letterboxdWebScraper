# Letterboxd Web Scraper

Web Scraper that allows you to save information (regarding films you've watched,
diary entries you've logged, etc.) to a .csv  or .txt file.

```commandline
python films.py --print tff 

Gathering letterboxd data, this may take a while (up to several minutes)

Printing: tff-Films

{'name': 'Pickpocket', 'director': ['Jia Zhangke'], 'year': 1997, 'language': ['Chinese'], 'country': ['China', 'Hong Kong'], 'runtime': 110, 'avg_rating': 3.88}
{'name': '24 Frames Per Second', 'director': ['Shirley Clarke'], 'year': 1977, 'language': ['English'], 'country': ['USA'], 'runtime': 3, 'avg_rating': 3.06}
{'name': 'Sambizanga', 'director': ['Sarah Maldoror'], 'year': 1972, 'language': ['Lingala', 'Portuguese'], 'country': ['Angola', 'France', 'Congo'], 'runtime': 102, 'avg_rating': 3.81}
{'name': 'Back and Forth', 'director': ['Michael Snow'], 'year': 1969, 'language': ['English'], 'country': ['Canada'], 'runtime': 52, 'avg_rating': 3.62}
{'name': 'Black Spiral', 'director': ['Aldo Tambellini'], 'year': 1969, 'language': ['English'], 'country': [], 'runtime': 11, 'avg_rating': -1.0}
{'name': 'Once Upon a Time in the West', 'director': ['Sergio Leone'], 'year': 1968, 'language': ['English'], 'country': ['Italy', 'USA'], 'runtime': 166, 'avg_rating': 4.39}
{'name': 'Black TV', 'director': ['Aldo Tambellini'], 'year': 1968, 'language': ['English'], 'country': ['USA'], 'runtime': 10, 'avg_rating': 3.52}
{'name': 'Black Trip 2', 'director': ['Aldo Tambellini'], 'year': 1967, 'language': ['English'], 'country': ['USA'], 'runtime': 3, 'avg_rating': -1.0}
{'name': "Black '67", 'director': ['Aldo Tambellini'], 'year': 1967, 'language': ['English'], 'country': [], 'runtime': 0, 'avg_rating': -1.0}
{'name': 'Black Plus X', 'director': ['Aldo Tambellini'], 'year': 1966, 'language': ['English'], 'country': ['USA'], 'runtime': 9, 'avg_rating': -1.0}
{'name': 'Black Trip', 'director': ['Aldo Tambellini'], 'year': 1965, 'language': ['No spoken language'], 'country': ['USA'], 'runtime': 4, 'avg_rating': -1.0}
{'name': 'Black Is', 'director': ['Aldo Tambellini'], 'year': 1965, 'language': ['English'], 'country': ['USA'], 'runtime': 4, 'avg_rating': -1.0}
{'name': 'Kustom Kar Kommandos', 'director': ['Kenneth Anger'], 'year': 1965, 'language': ['No spoken language'], 'country': ['USA'], 'runtime': 3, 'avg_rating': 3.57}
{'name': 'The Killers', 'director': ['Don Siegel'], 'year': 1964, 'language': ['English'], 'country': ['USA'], 'runtime': 93, 'avg_rating': 3.56}
{'name': 'Night Tide', 'director': ['Curtis Harrington'], 'year': 1961, 'language': ['English'], 'country': ['USA'], 'runtime': 84, 'avg_rating': 3.42}
{'name': 'Tunes of Glory', 'director': ['Ronald Neame'], 'year': 1960, 'language': ['English'], 'country': ['UK'], 'runtime': 106, 'avg_rating': 3.7}
{'name': 'Glimpses of the USA', 'director': ['Charles Eames', 'Ray Eames'], 'year': 1959, 'language': ['English'], 'country': ['USA'], 'runtime': 13, 'avg_rating': -1.0}
{'name': 'The Swindle', 'director': ['Federico Fellini'], 'year': 1955, 'language': ['Italian'], 'country': ['Italy', 'France'], 'runtime': 113, 'avg_rating': 3.7}
{'name': 'Crime Wave', 'director': ['André de Toth'], 'year': 1953, 'language': ['English'], 'country': ['USA'], 'runtime': 73, 'avg_rating': 3.69}
{'name': 'Apache Drums', 'director': ['Hugo Fregonese'], 'year': 1951, 'language': ['English', 'Spanish'], 'country': ['USA'], 'runtime': 75, 'avg_rating': 3.61}
{'name': 'The Flowers of St. Francis', 'director': ['Roberto Rossellini'], 'year': 1950, 'language': ['Italian', 'Latin'], 'country': ['Italy'], 'runtime': 87, 'avg_rating': 3.85}
{'name': 'Caught', 'director': ['Max Ophüls'], 'year': 1949, 'language': ['English'], 'country': ['USA'], 'runtime': 88, 'avg_rating': 3.64}
{'name': 'Force of Evil', 'director': ['Abraham Polonsky'], 'year': 1948, 'language': ['English'], 'country': ['USA'], 'runtime': 79, 'avg_rating': 3.64}
{'name': 'He Walked by Night', 'director': ['Alfred L. Werker'], 'year': 1948, 'language': ['English'], 'country': ['USA'], 'runtime': 79, 'avg_rating': 3.44}
{'name': 'The Woman on the Beach', 'director': ['Jean Renoir'], 'year': 1947, 'language': ['English'], 'country': ['USA'], 'runtime': 71, 'avg_rating': 3.38}
{'name': 'The Red House', 'director': ['Delmer Daves'], 'year': 1947, 'language': ['English'], 'country': ['USA'], 'runtime': 100, 'avg_rating': 3.33}
{'name': 'The Chase', 'director': ['Arthur Ripley'], 'year': 1946, 'language': ['English'], 'country': ['USA'], 'runtime': 86, 'avg_rating': 3.37}
{'name': 'The Killers', 'director': ['Don Siegel'], 'year': 1964, 'language': ['English'], 'country': ['USA'], 'runtime': 93, 'avg_rating': 3.56}
{'name': 'Shoeshine', 'director': ['Vittorio De Sica'], 'year': 1946, 'language': ['Italian', 'English'], 'country': ['Italy'], 'runtime': 87, 'avg_rating': 4.05}
{'name': 'Hallelujah', 'director': ['King Vidor'], 'year': 1929, 'language': ['English'], 'country': ['USA'], 'runtime': 100, 'avg_rating': 3.33}

```

### Data Options
| File to Call  | Description of Data Collected                    |
|---------------|--------------------------------------------------|
| ``films.py``  | Distinct films a user has seen                   |
| ``diary.py``  | Diary Entries (including each viewing of a film) |
| ``top250.py`` | Letterboxd's Top 250 Narrative Features List     |

### Arguments
``user`` is necessary for collecting data regarding a particular user (``films.py``, ``diary.py``)

| Argument           | Description               |
|--------------------|---------------------------|
| ``--print`` ``-p`` | Print data to console     |
| ``--csv`` ``-c``   | Write data to a .csv file |
| ``--txt`` ``-t``   | Write data to a .txt file |