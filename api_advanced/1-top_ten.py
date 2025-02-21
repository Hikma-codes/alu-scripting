#!/usr/bin/python3
import requests

def top_ten(subreddit):
    # Define the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set headers to avoid 403 Forbidden error (User-Agent is required by Reddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    # Try making the request and handle any errors
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If the response status code isn't 200, subreddit doesn't exist or is invalid
        if response.status_code != 200:
            print(None)
            return
        
        # If status code is 200, parse the JSON response
        data = response.json()
        
        # Extract the list of top 10 posts
        posts = data.get('data', {}).get('children', [])
        
        # Print the titles of the top 10 posts
        for post in posts:
            print(post.get('data', {}).get('title', ''))
    
    except Exception as e:
        # If there's an exception, print None
        print(None)

