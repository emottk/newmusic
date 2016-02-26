#New Music

This app uses the Soundcloud API to bring upcoming artists to the user. It displays artists with low follower counts along with a song to sample. A user can like an artist to view their profile later.

## Installation:

### System requirements

Newmusic requires [python3][https://www.python.org/download/releases/3.0/], [pip][https://pypi.python.org/pypi/pip], [virtualenvwrapper][https://virtualenvwrapper.readthedocs.org/en/latest/] and [postgresql][http://www.postgresql.org/].


To install system dependencies on OS X using [Homebrew](http://brew.sh/):

```bash
# Install system dependencies
brew install python3 postgresql
# pip will be installed by python3
pip install virtualenvwrapper

# virtualenvwrapper must be added to your shell profile to work
cat <<EOF >> ~/.bash_profile
export WORKON_HOME=~/.virtualenvs
[ -f /usr/local/bin/virtualenvwrapper.sh ] && . /usr/local/bin/virtualenvwrapper.sh
EOF
```

### Installing newmusic

```bash
# Clone the repository
git clone git@github.com:postlight/newmusic.git

cd newmusic

# Create a virtualenv and install dependencies via pip
mkvirtualenv newmusic
pip install -r requirements.txt

# Migrate your database
python manage.py migrate

# Run the development server
python manage.py runserver
```

You should now have a dev instance running at https://localhost:8000


## Deploying

Fill me out please!
