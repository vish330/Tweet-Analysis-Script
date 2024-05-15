from textblob import TextBlob
from gsheet_connect import authenticate
import gspread
import requests
import re  

def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def extract_hashtags(text):
    hashtags = re.findall(r'#(\w+)', text)  
    return hashtags

def main():
    gc = authenticate()
    workbook = gc.open('twitter_pro')
    
    try:
        sheet = workbook.worksheet('tweet_ui')
        
        url = "https://twitter154.p.rapidapi.com/user/tweets"
        querystring = {"username":"imVkohli","limit":"40","include_replies":"false","include_pinned":"false"}
        headers = {
            "X-RapidAPI-Key": "19d26a32aamshf4367558466025cp1b188ejsnfb8880d10855",
            "X-RapidAPI-Host": "twitter154.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        
        if response.status_code == 200:
            json_response = response.json()
            
            if 'results' in json_response:
                tweet_results = json_response['results']
                
                for i, tweet_info in enumerate(tweet_results):
                    tweet = tweet_info['text']
                    sentiment = get_sentiment(tweet)
                    hashtags = extract_hashtags(tweet)  
                    hashtags_str = ', '.join(hashtags)
                    
                    sheet.update_cell(i+2, 1, tweet)
                    sheet.update_cell(i+2, 2, sentiment)
                    sheet.update_cell(i+2, 3, hashtags_str)  
            else:
                print("No 'results' found in the response.")
        else:
            print(f"Failed to fetch tweets. Status code: {response.status_code}")
        
    except gspread.exceptions.APIError as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()

