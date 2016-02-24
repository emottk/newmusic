# New Music

This app uses the Soundcloud API to bring upcoming artists to the user. It displays artists with low follower counts along with a song to sample. A user can like an artist to view their profile later. 

##Installation

###Virtual environment

Make sure you add this to your $PATH:
```
export PATH ='/usr/local/bin:$PATH'
```
Then install virtualenvwrapper if you haven't already:
```
pip install virtualenvwrapper
```
Then set up your environment:
```
export WORKON_HOME=~/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv django
```
If you have not yet downloaded django, do so into your environment:
```
pip install django
```

###Installing newmusic

```
git clone git@github.com:postlight/newmusic.git
```
