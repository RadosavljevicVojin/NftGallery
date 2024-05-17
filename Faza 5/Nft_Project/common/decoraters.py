from django.contrib.auth.decorators import user_passes_test

def is_admin(user):

    if user.user_type=='admin':
        return True
    return False;

def is_creator(user):

    if user.user_type=='kreator':
        return True
    return False;

def is_creator_or_collector(user):

    if user.user_type=='kreator' or user.user_type=='kolekcionar':
        return True
    return False;
