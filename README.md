# Reality-Check 



Reality check is a Jupyter Notebook based CLI script that allows the user to search Twitter for keywords or hashtags and return an analysis of the sentiment (positive, negative, neutral) using machine learning. The script also has built in graphics features to create pie charts, circle charts, and word clouds for easier viewing. The script also allows for the user to see the most used words in these tweets. Finally the script creates n - grams (bi-grams and tri-grams) using a statistical model to predict what other words might be used in conjuction with the searched term.

Contents
========

 * [Uses](#Uses)
 * [Installation](#installation)
 * [Instructions](#Instructions)
 * [Example](#Example)
 * [What can I back up?](#what-can-i-back-up)
 * [Configuration](#configuration)
 * [Output Structure](#output-structure)
 * [Reinstalling Dotfiles](#reinstalling-dotfiles)
 * [Want to contribute?](#want-to-contribute)

### Uses

This script has many uses here are some examples:

+ Analysising the sentiment around "meme" stocks, cryptocurrencies, and NFTs.
+ Finding customer opinion on products or services.
  + Graphics features can be used to present these findings   
+ Informal polling for social issues.
  + Topics can be searched to find out how Twitter is reacting 
'Reality-Check' can be used for an abundance of purposes

### Installation
---
Download the repository to your local machine

*Please be advised that you will need a Twitter API key, information on how to obtain this can be found here https://developer.twitter.com/en/docs/twitter-api 

**Please see the attached for installs and libraries used. Pip install is used to add these libraries to your environment**

[![Installs][]


### Instructions
---
** After installation and integration of the Twitter API key, please see the following screenshot of cell 5 to get to the Command Line Interface **

[![cli][]


### Example
---

**The following is run with the keyword search of etherum and 150 tweets**

[![pie chart][]

* Circle Chart after the data has been cleaned up * 

[![circle chart][]

* Word count values *

[![word counts][]

* Word Cloud *

[![word cloud][]

** Bi and Tri grams **

[![n grams][]





### Reinstalling Dotfiles

To reinstall your dotfiles, clone your dotfiles repo and make sure your shallow-backup config path can be found at either `~/.config/shallow-backup.conf` or `$XDG_CONFIG_HOME/.shallow_backup.conf`. Set the `backup-path` key in the config to the path of your cloned dotfiles. Then run `$ shallow-backup -reinstall-dots`.

When reinstalling your dotfiles, the top level `.git/`, `.gitignore`, `img/` and `README.md` files and directories are ignored.

### Want to Contribute?
---

Check out `CONTRIBUTING.md` and the `docs` directory.
