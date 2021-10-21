# Reality-Check 



Reality check is a Jupyter Notebook based CLI script that allows the user to search Twitter for keywords or hashtags and return an analysis of the sentiment (positive, negative, neutral) using machine learning. There are built in functions to clean up the data pulled from Twitter. The script also has built in graphics features to create pie charts, circle charts, and word clouds for easier viewing. The script also allows for the user to see the most used words in these tweets. Finally the script creates n - grams (bi-grams and tri-grams) using a statistical model to predict what other words might be used in conjuction with the searched term.

Contents
========

 * [Uses](#Uses)
 * [Installation](#installation)
 * [Instructions](#Instructions)
 * [Example](#Example)
 * [Challenges Faced](#challenges-faced)
 * [Sources](#sources)
 * [Installation Documentation](#installation-documentation)
 * [Contributors](#contributors)
 * [License](#license)

## Uses

This script has many uses here are some examples:

+ Analysising the sentiment around "meme" stocks, cryptocurrencies, and NFTs.
+ Finding customer opinion on products or services.
  + Graphics features can be used to present these findings   
+ Informal polling for social issues.
  + Topics can be searched to find out how Twitter is reacting 
'Reality-Check' can be used for an abundance of purposes

## Installation
---
Download the repository to your local machine

*Please be advised that you will need a Twitter API key, information on how to obtain this can be found here (https://developer.twitter.com/en/docs/twitter-api)*

**Please see the attached for installs and libraries used. Pip install is used to add these libraries to your environment**

![Installs](https://github.com/joebary/Project-two_Team-4/blob/e179c0d7974d8110efcdd5d9a6f0c514481cd9f7/Images/installs.png)


### Instructions
---
**After installation and integration of the Twitter API key, please see the following screenshot of cell 5 to get to the Command Line Interface**

![cli](https://github.com/joebary/Project-two_Team-4/blob/e179c0d7974d8110efcdd5d9a6f0c514481cd9f7/Images/cli%20cell.png)


## Example
---

**The following is run with the keyword search of ethereum and 150 tweets**

![pie chart](https://github.com/joebary/Project-two_Team-4/blob/e179c0d7974d8110efcdd5d9a6f0c514481cd9f7/Images/pie%20chart.png)


**Circle Chart after the data has been cleaned up** 

![circle chart](https://github.com/joebary/Project-two_Team-4/blob/e179c0d7974d8110efcdd5d9a6f0c514481cd9f7/Images/circl%20chart.png)


**Word count values**

![word counts](https://github.com/joebary/Project-two_Team-4/blob/e179c0d7974d8110efcdd5d9a6f0c514481cd9f7/Images/word%20counts.png)


**Word Cloud**

![word cloud](https://github.com/joebary/Project-two_Team-4/blob/e179c0d7974d8110efcdd5d9a6f0c514481cd9f7/Images/word%20cloud.png)


**Bi and Tri grams**

![n grams](https://github.com/joebary/Project-two_Team-4/blob/e179c0d7974d8110efcdd5d9a6f0c514481cd9f7/Images/n%20grams.png)

## Challenges Faced
---
There were two main challenges faced in this project .

1. Amazon Lambda and Lex
2. Social Media Data

The original idea for this project was to create an Amazon Lex bot that the user would interact with. We were able to get the bot set up, but the back end Lambda function proved difficult to work with, and the bot did not work. Ultimately, we were able to get more functionality and consistancy out of the CLI.


We were able to get data from the Twitter API, but they do ask a lot of question and it takes an amount of time to get access. API data for Reddit and Facebook are also available, and the code could be modified to take in data from those two sources as well. More than likely a libary such as Tweepy would need to be imported to make sure the data will funciton properly within python.




## Sources
---



## Installation Documentation
---
textblob -https://textblob.readthedocs.io/en/dev/
tweepy -https://www.tweepy.org
matplotlib -https://matplotlib.org
pandas -https://pandas.pydata.org
numpy -https://numpy.org
nltk -https://www.nltk.org
pycountry -https://pypi.org/project/pycountry/
dotenv -https://pypi.org/project/python-dotenv/
requests -https://pypi.org/project/requests/
json  -https://www.json.org/json-en.html
wordcloud -https://pypi.org/project/wordcloud/#:~:text=The%20wordcloud%20library%20is%20MIT%20licenced%2C%20but%20contains,the%20font_path%20variable%20when%20creating%20a%20WordCloud%20object.
PIL -http://2017.compciv.org/guide/topics/python-nonstandard-libraries/pillow.html
langdetect -https://pypi.org/project/langdetect/
sklearn -https://scikit-learn.org/stable/index.html

## Contributors
---
Henry Wilcox - haw299@nyu.edu
Sean Patel - seanpatel076@gmail.com
Youssef Said - joebary2008@gmail.com
Kian Momeni - KMomeni97@gmail.com

**With Special Thanks to our TA**
Mayur Amrutiya -mayuramrutiya325@gmail.com


## License
---
Public 
