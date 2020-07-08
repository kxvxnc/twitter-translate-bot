# Tweet Translator Bot

This bot monitors a user for new tweets every n seconds and automatically 
replies with a translated version of the original tweet.


## Demo
![Tweet Translate Demo](https://github.com/kxvxnc/images/blob/master/translatebotdemo.gif)


## Installing / Getting started

```
git clone https://github.com/kxvxnc/twitter-translate-bot.git
cd path/to/twitter-translate-bot/
pip install requirements.txt
```

We're not done setting up yet! We still need some keys and tokens to run this project.


### Initial Configuration

1. Apply for a twitter [developer account](https://developer.twitter.com/en/application/use-case) if you haven't already
2. Create a new project on the dashboard with Read and Write permissions
3. Generate your consumer keys and Authentication Tokens(make sure these are created with read/write permissions) 
and put them in the `config.json` file
```
    "consumer_key": "YOUR API KEY",
    "consumer_secret": "YOUR API SECRET",
    "access_token": "YOUR ACCESS TOKEN",
    "access_token_secret": "YOUR ACCESS TOKEN SECRET",
```
4. Create a [google cloud console project](https://cloud.google.com/translate/docs/basic/setup-basic) 
and enable the google translate API.
5. Download the private key as JSON and paste the full path in `translate.py`
```
credential_path = r"PATH TO GOOGLE CLOUD CREDENTIAL FILE"
```


## Features

Monitors a user for new tweets every n seconds
* Once the change is detected, a translated tweet will be sent as a reply to the new tweet
* Ignores tweets/retweets/replies with no text or only images
* Filters out t.co hyperlinks to avoid relinking to an original tweet and reposting images
* Supports multiple users
* Easy to understand logging and error handling


## Configuration

Edit the `config.json` for custom configuration
* The delay is how many seconds it sleeps between monitoring
* Translates to any language available in `languages.txt`
* You can choose if you want to monitor for replies by setting replies to true or false
* You are able to add more than 1 user; just follow the format
* Keep the requests to 900 every 15 minutes; don't exceed 1 request per second


## Contributing

If you would like to contribute, please fork the repository and use a feature branch. 
Pull requests are welcome.


## Deploying / Publishing

This project currently only works on localhost and has not been tested/deployed for large-scale use.


## Links

- Repository: https://github.com/kxvxnc/twitter-translate-bot/
- Issue tracker: https://github.com/kxvxnc/twitter-translate-bot/issues
- Related projects:
  - Instagram Monitor: https://github.com/kxvxnc/instagram-monitor/


## Licensing

The code in this project is licensed under MIT license and can be found in `LICENSE.txt`.
