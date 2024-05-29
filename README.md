## Letterboxd Web Scraper

Web Scraper that allows you to save information (regardingfilms you've watched,
diary entries you've logged, etc.) to a .csv  or .txt file.

```commandline
python diary.py --print tff

Gathering letterboxd data, this may take a while (up to several minutes)

Printing: tff-Diary

{'name': 'The Killers', 'viewing_date': '2023-06-29', 'review': 'Join us for a free onli', 'rating': '0', 'tags': [],
'rewatch': False, 'info': {'director': ['Don Siegel'], 'year': 1964, 'language': ['English'], 'country': ['USA'], 
'runtime': 93, 'avg_rating': 3.56}}
{'name': 'The Killers', 'viewing_date': '2023-06-29', 'review': 'Join us for a free onli', 'rating': '0', 'tags': [],
'rewatch': False, 'info': {'director': ['Don Siegel'], 'year': 1964, 'language': ['English'], 'country': ['USA']
'runtime': 93, 'avg_rating': 3.56}}
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