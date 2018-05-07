# Football LiveScore
Livescore Scrape

## Requirements 
Download [Chrome WebDriver](http://chromedriver.chromium.org/downloads) and save it in the app directory.

## Installation
```
$ git clone https://github.com/dedenbangkit/football-score.git
$ cd football-score
$ pip install -r requirements.txt
```
note: you can also install the requirements to isolated [virtualenv](https://virtualenv.pypa.io/en/stable/)

## Usage
```
// Run the server
$ python app.py
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 953-947-058

// Call the app
$ curl http://127.0.0.1:5000/2018-05-06
[
  {
    "date": "May 5 2018",
    "league": "England - Premier League",
    "match": [
        {
            "away": "Everton",
            "home": "Southampton",
            "score": "1 - 1",
            "time": "FT"
        },
        {...}
    ]
  },
  {...}
]
```

## Dependencies
- [Flask 0.12](http://flask.pocoo.org/)
- [Selenium 3.11.0](http://selenium-python.readthedocs.io/)
