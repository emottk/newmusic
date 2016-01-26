from django.conf import settings
from django.contrib.auth.models import User
from newmusic.main.models import Artist, Opinion

def unique_list(request):
    user = request.user
    opinions = user.opinion_set.all()
    unique = set()
    for o in opinions:
        unique.add(o)
    ulist = list(unique)
    return ulist

def sort_true(request):
    unique = unique_list(request)
    true_list = []
    for o in unique:
        if o.opinion == True:
            true_list.append(o)
    return true_list

def sort_false(request):
    unique = unique_list(request)
    false_list = []
    for o in unique:
        if o.opinion == False:
            false_list.append(o)
    return false_list
