facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Share':3},
    {'Likes': 4, 'Comments': 2},
    {'Likes': 1, 'Comments': 1},
    {'Likes': 19, 'Comments': 3},

]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['likes']
    except KeyError:
        total_likes += 0

print(total_likes)
