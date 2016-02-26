#New Music

This app uses the Soundcloud API to bring upcoming artists to the user. It displays artists with low follower counts along with a song to sample. A user can like an artist to view their profile later.

##Installation:

###Virtual environment

Make sure you add this to your $PATH:
```
export PATH ='/usr/local/bin:$PATH'
```
Install virtualenvwrapper if you haven't already:
```
pip install virtualenvwrapper
```
Set up your environment:
```
export WORKON_HOME=~/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv django
```
This app uses Django 1.9.2 and Python 3.5.1. Make sure you specify these in your environment.

###Installing newmusic

```
git clone git@github.com:postlight/newmusic.git
```
