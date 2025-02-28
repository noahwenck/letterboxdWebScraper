# Letterboxd Web Scraper
Easily export User/List data from Letterboxd.com!

## Installation
1. Clone the repository:
    ```
    git clone git@github.com:noahwenck/letterboxdWebScraper.git
    ```
2. Install the required dependencies
    ```
    pip install -r requirements.txt
    ```
   

## Running
There are a few different ways to use this project:
1. Connect to [noda](https://github.com/noahwenck/noda) to import data to it.
   1. Run:
        ```
        python shinoda.py
        ```
      This will start up the Shinoda Flask API. Connects to port 5000 by default.
   2. Verify successful connection:
        ```
        curl http://localhost:5000/ping 
        ```
      If successful, you will see "alive!".
2. Use the utility scripts to collect data from Letterboxd, and print it to the terminal or save to a file. 
   1. Look through the `--UTIL` table to see what you want to do with the data (print, save, etc.).
   2. For films that a User has interacted with:
      1. Read through the [User Sections](#user-sections) table to determine which User section you would like to export.
      2. Run:
        ```
        python user.py --UTIL <LETTERBOXD_USERNAME> <SECTION>
        ```
        For example, to print the films of user tff to the terminal:
        ```
        python user.py -p tff films
        ```
   3. For films in a list:
      1. Run:
        ```
        python list.py --UTIL <LETTERBOXD_LIST_URL
        ```
        For example, to print the films of user michaelmann's (Yes, the real Michal Mann) 
         14 Favorite Films in no Particular Order List to the terminal:
        ```
        python list.py -p https://letterboxd.com/michaelmann/list/14-favorite-films-in-no-particular-order/
        ```


## User Sections
|    Section    | Description of Data                              |
|:-------------:|--------------------------------------------------|
|   ``films``   | Distinct films a user has seen                   |
|   ``diary``   | Diary Entries (including each viewing of a film) |
| ``watchlist`` | Films on a user's watchlist                      |
|   ``likes``   | Films a user has marked as liked                 |


## Utility Arguments
Use these to define how you want the data outputted. Utility arguments are completely optional.

|        Argument         | Description                                       |
|:-----------------------:|---------------------------------------------------|
|   ``-p`` ``--print``    | Print data to console                             |
|    ``-c`` ``--csv``     | Write data to a .csv file                         |
|    ``-t`` ``--txt``     | Write data to a .txt file                         |
| ``-e`` ``--everything`` | Collect everything (Includes Cast + Crew in data) |