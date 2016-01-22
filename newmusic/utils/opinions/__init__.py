from django.conf import settings
from django.contrib.auth.models import User
from newmusic.main.models import Artist, Opinion

def sort_opinion(request):
    user = request.user
    opinions = user.opinion_set.all()
    true_list = []
    false_list = []
    for o in opinions:
        if o.opinion == True:
            true_list.append(o)
        else:
            false_list.append(o)
    return true_list, false_list
