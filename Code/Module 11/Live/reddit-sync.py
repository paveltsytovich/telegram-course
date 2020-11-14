# (c) TICSIA
#
#
import requests
import datetime
def get_reddit_top(subreddit,numposts):
    response = requests.get('https://www.reddit.com/r/' + subreddit + '/top.json?=top&t=day&limit=' + str(numposts))
    if response.status_code == 200:
        json = response.json()
        for i in json['data']['children']:
            score = i['data']['score']
            title = i['data']['title']
            link = i['data']['url']
            print('\t' + str(score) + ':' + title + '\n\t\t('+ link + ')')
        
print(datetime.datetime.now().strftime("%A %B %d %I:%M %p"))
print('-------------------')
get_reddit_top('python',3),
get_reddit_top('programming',4),
get_reddit_top('asyncio',2),
get_reddit_top('dailyprogrammer',1)

