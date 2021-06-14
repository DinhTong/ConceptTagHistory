# ConceptTagHistory
Life is hard, nothing is perfect. I was given these 2 raw datasets and my task was to generate a full history log as shown. I had to get it done in MySQL 5.6.10 but you don't have to. 
1. One customer can recieve multiple tags at the same time
2. We are only interested in INVENTORY tag type

## Create Virtual Environment and install dependencies

## mac OS
`which python3`

For me it's 
`/usr/local/bin/python3`

`pwd`
For me it's
`/Users/siliconrob/projects/ConceptTagHistory`

### Now setup the `venv`
- `/usr/local/bin/python3 -m venv $(pwd)/venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python src/main.py`

And.... YAY!
When you are done deactivate the `venv`
- `deactivate`

## Windows
- `c:\>C:\Python39\python -m venv C:\projects\ConceptTagHistory\venv`
- `pip install requirements.txt`
