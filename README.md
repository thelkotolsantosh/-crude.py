# Purchase request register

Requests have stable numeric IDs. Each change is saved in requests.sqlite. Pass --db before the command to choose a different file.

## Run locally

Use Python 3.8 or newer. Run these commands in the project directory.

```sh
python app.py add Roller
python app.py edit 1 Handle
```

Run `python app.py --help` for options and `python -m unittest -v` to check the command-line workflow.
