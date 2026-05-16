# Movie Info Finder

A simple Python movie lookup tool with a Flask web interface.

## Files

- `j.py` - Python module and CLI script for querying the OMDb API.
- `app.py` - Flask app that serves a web page and uses `j.py` to fetch movie details.
- `templates/index.html` - Web page UI for searching movies.
- `requirements.txt` - Required Python packages.

## Setup

1. Get an OMDb API key from https://www.omdbapi.com/
2. Set the environment variable `OMDB_API_KEY`.

PowerShell:

```powershell
$env:OMDB_API_KEY = "your_api_key_here"
```

## Run the web app

```powershell
cd "c:\Users\tejam\Documents\Projects on 6th\Python Projects\Movie Info Finder"
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:5000` in your browser.

## Run the CLI tool

```powershell
python j.py
```

The CLI will prompt for a movie title and print the movie information.
