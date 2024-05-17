from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render

from common.decoraters import is_creator


# Create your views here.


@login_required(login_url='/accounts/error')
@user_passes_test(is_creator, login_url='/accounts/error')
def create_nft(request):

    return render(request, 'create_nft.html')
