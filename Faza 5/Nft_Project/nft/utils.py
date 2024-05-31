from .models import *
from exhibitions.models import *

def first_time_grading(nft, reg_user):
    all_grades = Ocena.objects.filter(idkor=reg_user, idnft=nft)
    if all_grades:
        return False
    return True

def get_exhibitions_from_nft(nft):
    lists_where_nft_belongs = [b.idlis for b in Pripada.objects.filter(idnft=nft)]
    return [exhibition for exhibition in Izlozba.objects.all() if exhibition.idlis in lists_where_nft_belongs]

def update_exhibition_grade(exhibition, exhibition_nfts):

    print("\n\nRACUNAM PROSECNU OCENU IZLOZBE!\n\n")

    print("\n\nNftjevi iz izlozbe su:\n")

    graded_len = 0
    sum_grade = 0

    for nft in exhibition_nfts:
        print("Nft je " + str(nft))
        if nft.prosecnaocena > 0:
            print("Prosecna ocena nft je " + str(nft.prosecnaocena))
            graded_len += 1
            sum_grade += nft.prosecnaocena
        else:
            print("Ovaj nft nije ocenjen")


    print("\nSum grade = " + str(float(sum_grade)))
    print("\nGradelen = " + str(graded_len))
    if graded_len > 0:
        exhibition.prosecnaocena = float(sum_grade) / graded_len
    else:
        exhibition.prosecnaocena = 0

    exhibition.save()

    print("\nprosecna ocena izlozbe je " + str(exhibition.prosecnaocena))
    """
    grades = Ocena.objects.filter(idnft__in=exhibition_nfts)

    if grades.exists():
        exhibition.prosecnaocena = float(sum(grade.ocena for grade in grades)) / len(grades)
        print("\nBroj ocena apdejtovane izlozbe je " + str(len(grades)))
    else:
        exhibition.prosecnaocena = 0
        print("\nBroj ocena apdejtovane izlozbe je 0" + str(len(grades)))

    exhibition.save()

    print("Ocene apdejtovane izlozbe su")
    for grade in grades:
        print("Ocena: " + str(grade.ocena))

    print("\nBroj ocena apdejtovane izlozbe je" + str(len(grades)))
    print("\n Prosek : " + str(exhibition.prosecnaocena))
    """

def only_in_collection(nft):
    lists = Listanft.objects.filter(idvla=nft.idvla)

    # Prebrojavamo koliko listi sadrži dati NFT
    count = Pripada.objects.filter(idnft=nft, idlis__in=lists).count()

    # Vraćamo True ako NFT pripada samo jednoj listi, inače False
    return count == 1



def denied_access_to_the_nft(request, nft):
    if only_in_collection(nft) and request.user.username!=nft.idvla.idkor.username:
        return True
    else:
        return False

def get_nfts_from_exhibition(exhibition):
    nfts = []
    if exhibition:
        belong = Pripada.objects.filter(idlis=exhibition.idlis)
        nfts = [b.idnft for b in belong]

    return nfts


def update_nft_all_exhibitions_with_grades(nft):
    exhibitions = get_exhibitions_from_nft(nft)
    for exhibition in exhibitions:
        exhibition_nfts = get_nfts_from_exhibition(exhibition)
        update_exhibition_grade(exhibition, exhibition_nfts)

    return
