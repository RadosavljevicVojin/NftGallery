from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from common.decoraters import is_creator_or_collector


# Create your views here.
def index(request):
    return render(request, "index.html")




@login_required(login_url='/accounts/error')
@user_passes_test(is_creator_or_collector, login_url='/accounts/error')
def create_exhibition(request):

    return render(request, 'create_exhibition.html')
