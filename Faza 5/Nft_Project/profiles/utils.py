from accounts.models import Korisnik
from profiles.models import Registrovanikorisnik


def create_main_context(request, username):

    user = Korisnik.objects.get(username=username)
    context = dict()
    context["username"] = user.username
    context["image"] = Registrovanikorisnik.objects.get(idkor=user).slika.url
    context["type"] = user.user_type
    context["myprofile"] = False
    if user.username == request.user.username:
        context["myprofile"] = True

    return context

