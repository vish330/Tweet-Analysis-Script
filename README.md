# Tweet-Analysis-Script

This Python script fetches tweets from a Twitter user, analyzes their sentiment using TextBlob, and extracts hashtags. It then updates a Google Sheet with the tweet text, sentiment, and extracted hashtags.

Prerequisites
1.Python 3
2.textblob library
3.gspread library
4.requests library
5.re module (for regular expression operations)

Setup
1.Install the required Python libraries:
2.Make sure you have a Google Cloud Platform project set up with the Google Sheets API enabled.
3.Obtain OAuth2 credentials for accessing the Google Sheets API. Place the credentials file (credentials.json) in the same directory as the script.
4.Create a Google Sheet named twitter_pro with a worksheet named tweet_ui.
5.Set up your RapidAPI account and obtain an API key for accessing the Twitter API.
6.Replace the placeholder values in the script with your actual Twitter API key and Twitter username.
