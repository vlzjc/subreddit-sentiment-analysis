import json
import pandas as pd

# Load the JSON data from the saved file
with open('showerthoughts_posts.txt', 'r') as txt_file:
    data = json.load(txt_file).get('data', [])

# Extract required fields from JSON data
posts = []
for post in data:
    posts.append({
        'author_name': post['author']['name'],
        'is_nsfw': post['nsfw'],
        'comments_count': post['comments'],
        'score': post['score'],
        'shares': post['shares'],
        'title': post['title'],
        'upvote_ratio': post['upvoteRatio'],
        'url': post['url']
    })

# Convert to DataFrame
df = pd.DataFrame(posts)

# Save to CSV
df.to_csv('showerthoughts_posts.csv', index=False)

print("Post data loaded from showerthoughts_posts.txt and saved to showerthoughts_posts.csv")

print(df.head())