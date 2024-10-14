# Letterboxd Web Scraper

Web Scraper that allows you to save information (regarding films you've watched,
diary entries you've logged, etc.) to a .csv  or .txt file.

### ``user.py``
Collect the films that a user has interacted with.

|    Section    | Description of Data                              |
|:-------------:|--------------------------------------------------|
|   ``films``   | Distinct films a user has seen                   |
|   ``diary``   | Diary Entries (including each viewing of a film) |
| ``watchlist`` | Films on a user's watchlist                      |
|   ``likes``   | Films a user has marked as liked                 |

Syntax: ```> python user.py --UTIL USER SECTION ```

Example: 
```commandline
> python user.py -p tff films

Gathering letterboxd data, this may take a while. (up to several minutes)

Printing: tff-Films

{'name': 'Pickpocket', 'director': ['Jia Zhangke'], 'year': 1997, 'primary_language': 'Chinese', 'spoken_language': ['Chinese'], 'country': ['China', 'Hong Kong'], 'runtime': 110, 'avg_rating': 3.88}
{'name': 'The Boys from Fengkuei', 'director': ['Hou Hsiao-hsien'], 'year': 1983, 'primary_language': 'Chinese', 'spoken_language': ['Chinese'], 'country': ['Taiwan'], 'runtime': 98, 'avg_rating': 3.76}
{'name': '24 Frames Per Second', 'director': ['Shirley Clarke'], 'year': 1977, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 3, 'avg_rating': 3.06}
{'name': 'Sambizanga', 'director': ['Sarah Maldoror'], 'year': 1972, 'primary_language': 'Lingala', 'spoken_language': ['Lingala', 'Portuguese'], 'country': ['Angola', 'France', 'Congo'], 'runtime': 102, 'avg_rating': 3.82}
{'name': 'Lions Love', 'director': ['Agnès Varda'], 'year': 1969, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA', 'France'], 'runtime': 110, 'avg_rating': 3.41}
{'name': 'Back and Forth', 'director': ['Michael Snow'], 'year': 1969, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['Canada'], 'runtime': 52, 'avg_rating': 3.64}
{'name': 'Black Spiral', 'director': ['Aldo Tambellini'], 'year': 1969, 'primary_language': 'English', 'spoken_language': ['English'], 'country': [], 'runtime': 11, 'avg_rating': -1.0}
{'name': 'Once Upon a Time in the West', 'director': ['Sergio Leone'], 'year': 1968, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['Italy', 'USA'], 'runtime': 166, 'avg_rating': 4.39}
{'name': 'Black TV', 'director': ['Aldo Tambellini'], 'year': 1968, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 10, 'avg_rating': 3.52}
{'name': 'Black Trip 2', 'director': ['Aldo Tambellini'], 'year': 1967, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 3, 'avg_rating': -1.0}
{'name': "Black '67", 'director': ['Aldo Tambellini'], 'year': 1967, 'primary_language': 'English', 'spoken_language': ['English'], 'country': [], 'runtime': 0, 'avg_rating': -1.0}
{'name': 'Black Plus X', 'director': ['Aldo Tambellini'], 'year': 1966, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 9, 'avg_rating': -1.0}
{'name': 'Black Trip', 'director': ['Aldo Tambellini'], 'year': 1965, 'primary_language': 'No spoken language', 'spoken_language': ['No spoken language'], 'country': ['USA'], 'runtime': 4, 'avg_rating': -1.0}
{'name': 'Black Is', 'director': ['Aldo Tambellini'], 'year': 1965, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 4, 'avg_rating': -1.0}
{'name': 'Kustom Kar Kommandos', 'director': ['Kenneth Anger'], 'year': 1965, 'primary_language': 'No spoken language', 'spoken_language': ['No spoken language'], 'country': ['USA'], 'runtime': 3, 'avg_rating': 3.57}
{'name': 'The Killers', 'director': ['Don Siegel'], 'year': 1964, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 93, 'avg_rating': 3.56}
{'name': 'Night Tide', 'director': ['Curtis Harrington'], 'year': 1961, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 84, 'avg_rating': 3.43}
{'name': 'Tunes of Glory', 'director': ['Ronald Neame'], 'year': 1960, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['UK'], 'runtime': 106, 'avg_rating': 3.7}
{'name': 'Glimpses of the USA', 'director': ['Charles Eames', 'Ray Eames'], 'year': 1959, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 13, 'avg_rating': -1.0}
{'name': 'Orgosolo’s Shepherds', 'director': ['Vittorio De Seta'], 'year': 1958, 'primary_language': 'Italian', 'spoken_language': ['Italian'], 'country': ['Italy'], 'runtime': 11, 'avg_rating': 3.85}
{'name': '7 Men from Now', 'director': ['Budd Boetticher'], 'year': 1956, 'primary_language': 'English', 'spoken_language': ['English', 'French'], 'country': ['USA'], 'runtime': 78, 'avg_rating': 3.78}
{'name': 'The Swindle', 'director': ['Federico Fellini'], 'year': 1955, 'primary_language': 'Italian', 'spoken_language': ['Italian'], 'country': ['Italy', 'France'], 'runtime': 113, 'avg_rating': 3.71}
{'name': 'Crime Wave', 'director': ['André de Toth'], 'year': 1953, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 73, 'avg_rating': 3.69}
{'name': 'Apache Drums', 'director': ['Hugo Fregonese'], 'year': 1951, 'primary_language': 'English', 'spoken_language': ['English', 'Spanish'], 'country': ['USA'], 'runtime': 75, 'avg_rating': 3.61}
{'name': 'The Flowers of St. Francis', 'director': ['Roberto Rossellini'], 'year': 1950, 'primary_language': 'Italian', 'spoken_language': ['Italian', 'Latin'], 'country': ['Italy'], 'runtime': 87, 'avg_rating': 3.85}
{'name': 'Caught', 'director': ['Max Ophüls'], 'year': 1949, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 88, 'avg_rating': 3.65}
{'name': 'Force of Evil', 'director': ['Abraham Polonsky'], 'year': 1948, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 79, 'avg_rating': 3.65}
{'name': 'He Walked by Night', 'director': ['Alfred L. Werker'], 'year': 1948, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 79, 'avg_rating': 3.44}
{'name': 'The Woman on the Beach', 'director': ['Jean Renoir'], 'year': 1947, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 71, 'avg_rating': 3.38}
{'name': 'The Red House', 'director': ['Delmer Daves'], 'year': 1947, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 100, 'avg_rating': 3.34}
{'name': 'The Chase', 'director': ['Arthur Ripley'], 'year': 1946, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 86, 'avg_rating': 3.38}
{'name': 'The Killers', 'director': ['Don Siegel'], 'year': 1964, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 93, 'avg_rating': 3.56}
{'name': 'Shoeshine', 'director': ['Vittorio De Sica'], 'year': 1946, 'primary_language': 'Italian', 'spoken_language': ['Italian', 'English'], 'country': ['Italy'], 'runtime': 91, 'avg_rating': 4.05}
{'name': 'Story of G.I. Joe', 'director': ['William A. Wellman'], 'year': 1945, 'primary_language': 'English', 'spoken_language': ['English', 'Italian'], 'country': ['USA'], 'runtime': 108, 'avg_rating': 3.52}
{'name': "L'Atalante", 'director': ['Jean Vigo'], 'year': 1934, 'primary_language': 'French', 'spoken_language': ['French'], 'country': ['France'], 'runtime': 89, 'avg_rating': 3.98}
{'name': 'Hallelujah', 'director': ['King Vidor'], 'year': 1929, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 100, 'avg_rating': 3.33}

```

### ``list.py``
Collect films from any list on Letterboxd. 

Syntax: ```> python list.py --UTIL URL```

Example: 
``` commandline
> python list.py -p https://letterboxd.com/michaelmann/list/14-favorite-films-in-no-particular-order/

Gathering Letterboxd data, this may take a while (up to several minutes)

Printing: 14-Favorite-Films-in-no-particular-order-(except-Potemkin)

{'name': 'Battleship Potemkin', 'director': ['Sergei Eisenstein'], 'year': 1925, 'primary_language': 'No spoken language', 'spoken_language': ['No spoken language'], 'country': ['USSR'], 'runtime': 75, 'avg_rating': 4.0, 'genre': ['History', 'War', 'Drama']}
{'name': 'Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb', 'director': ['Stanley Kubrick'], 'year': 1964, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['UK', 'USA'], 'runtime': 95, 'avg_rating': 4.31, 'genre': ['Comedy', 'War']}
{'name': 'Biutiful', 'director': ['Alejandro González Iñárritu'], 'year': 2010, 'primary_language': 'Spanish', 'spoken_language': ['Spanish', 'Cantonese', 'Chinese', 'Wolof'], 'country': ['Mexico', 'Spain', 'USA'], 'runtime': 148, 'avg_rating': 3.83, 'genre': ['Drama']}
{'name': 'Raging Bull', 'director': ['Martin Scorsese'], 'year': 1980, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 129, 'avg_rating': 4.25, 'genre': ['Drama']}
{'name': 'Incendies', 'director': ['Denis Villeneuve'], 'year': 2010, 'primary_language': 'French', 'spoken_language': ['French', 'Arabic', 'English'], 'country': ['Canada', 'France'], 'runtime': 131, 'avg_rating': 4.41, 'genre': ['Mystery', 'War', 'Drama']}
{'name': 'Pale Flower', 'director': ['Masahiro Shinoda'], 'year': 1964, 'primary_language': 'Japanese', 'spoken_language': ['Japanese'], 'country': ['Japan'], 'runtime': 96, 'avg_rating': 4.01, 'genre': ['Romance', 'Crime']}        
{'name': "L'Atalante", 'director': ['Jean Vigo'], 'year': 1934, 'primary_language': 'French', 'spoken_language': ['French'], 'country': ['France'], 'runtime': 89, 'avg_rating': 3.98, 'genre': ['Romance', 'Drama', 'Comedy']}
{'name': 'The Asphalt Jungle', 'director': ['John Huston'], 'year': 1950, 'primary_language': 'English', 'spoken_language': ['English', 'German'], 'country': ['USA'], 'runtime': 112, 'avg_rating': 3.86, 'genre': ['Drama', 'Crime']} 
{'name': 'Poor Things', 'director': ['Yorgos Lanthimos'], 'year': 2023, 'primary_language': 'English', 'spoken_language': ['English', 'French', 'Portuguese'], 'country': ['Ireland', 'UK', 'USA'], 'runtime': 142, 'avg_rating': 4.04, 'genre': ['Romance', 'Science Fiction', 'Comedy']}
{'name': 'Apocalypse Now', 'director': ['Francis Ford Coppola'], 'year': 1979, 'primary_language': 'English', 'spoken_language': ['English', 'Khmer', 'French', 'Vietnamese'], 'country': ['USA'], 'runtime': 147, 'avg_rating': 4.44, 'genre': ['Drama', 'War']}
{'name': 'Sweet Smell of Success', 'director': ['Alexander Mackendrick'], 'year': 1957, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 97, 'avg_rating': 4.24, 'genre': ['Drama']}       
{'name': 'The Hurt Locker', 'director': ['Kathryn Bigelow'], 'year': 2008, 'primary_language': 'English', 'spoken_language': ['English', 'Arabic', 'Turkish'], 'country': ['USA'], 'runtime': 131, 'avg_rating': 3.75, 'genre': ['Drama', 'War', 'Thriller']}
{'name': 'Out of the Past', 'director': ['Jacques Tourneur'], 'year': 1947, 'primary_language': 'English', 'spoken_language': ['English'], 'country': ['USA'], 'runtime': 97, 'avg_rating': 4.11, 'genre': ['Thriller', 'Romance', 'Crime']}
{'name': "Pan's Labyrinth", 'director': ['Guillermo del Toro'], 'year': 2006, 'primary_language': 'Spanish', 'spoken_language': ['Spanish'], 'country': ['Mexico', 'Spain', 'USA'], 'runtime': 118, 'avg_rating': 4.16, 'genre': ['War', 'Fantasy', 'Drama']}
```

### Utility Arguments
Use these to define how you want the data outputted.

|        Argument         | Description                                      |
|:-----------------------:|--------------------------------------------------|
|   ``-p`` ``--print``    | Print data to console                            |
|    ``-c`` ``--csv``     | Write data to a .csv file                        |
|    ``-t`` ``--txt``     | Write data to a .txt file                        |
| ``-e`` ``--everything`` | Collect everything (Include Cast + Crew in data) |

---
### Connect to Noda

To use in tandem with [NodaApp](https://github.com/noahwenck/NodaApp), run the following to set up the
flask app that Noda communicates with. 

```
py -m flask --app noda run
```

Connects to port 5000 by default. Feel free to verify connection via curl:

```
curl http://localhost:5000/ping
```
