# Twitter Translate Bot
[![CodeFactor](https://www.codefactor.io/repository/github/kxvxnc/twitter-translate-bot/badge)](https://www.codefactor.io/repository/github/kxvxnc/twitter-translate-bot)

This bot monitors user(s) for new tweets every x seconds and automatically replies with a translated version of the original tweet.


## Features

* Monitors a user for new tweets and replies with a translated version of tweet
* Supports multiple users
* Ignores tweets/retweets/replies with no text or only images
* Filters out t.co hyperlinks to avoid relinking and reposting
* Clear and concise logging/error handling messages


## Installation

```
git clone https://github.com/kxvxnc/twitter-translate-bot.git
cd path/to/twitter-translate-bot/
```
We're not done yet! We still need some tokens and configurations to run it.


## Configuration

1. Apply for a twitter [developer account](https://developer.twitter.com/en/application/use-case) and create a new 
project on the dashboard with Read and Write permissions
2. Create a `.env` file in the root directory similar to the `.env.example` file and fill in your keys
```
CONSUMER_KEY=KEY
CONSUMER_SECRET=SECRET
ACCESS_TOKEN=TOKEN
ACCESS_TOKEN_SECRET=TOKEN_SECRET
```
3. Create a [Google Cloud console project](https://cloud.google.com/translate/docs/basic/setup-basic) and enable the google translate API.
4. Download the private key as a JSON file into the `src` directory and edit the filename in the `.env` file
```
CREDENTIAL_PATH=src/gcloud_filename.json
```
5. Edit the `config.json` for custom configuration
* `"delay_seconds"` is how many seconds it sleeps between monitoring
* `"user"` is the @ of the user you want to monitor
* You can choose if you want to monitor for replies by setting `"replies"` to `true` or `false`
* `"lang"` can be any language in `languages.txt`
* You are able to add more than 1 user; just add a new object

Note: Keep the requests to 900 every 15 minutes; don't exceed 1 request per second (Twitter API Rate Limit)


## Running / Deploying

This project can be ran on localhost and Docker but has not been tested for large-scale use.

### Localhost
1. `pip install pipenv`
2. `pipenv install`
3. `pipenv run python3 src/main.py`

### Docker
1. `docker build -t image_name .`
2. `docker run --env-file .env image_name`


## Contributing

If you would like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.


## Links

- Repository: https://github.com/kxvxnc/twitter-translate-bot/
- Issue tracker: https://github.com/kxvxnc/twitter-translate-bot/issues
- Related projects:
  - Instagram Monitor: https://github.com/kxvxnc/instagram-monitor/


## Licensing

The code in this project is licensed under MIT license and can be found in `LICENSE.txt`.
