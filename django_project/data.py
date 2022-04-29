from accounts.models import UserModel

def checkRes(request, us, num_page, isSave=True):
    if(num_page == 1):
       return lessons1(request, us, isSave)
    elif num_page == 2:
        return lessons2(request, us, isSave)
    elif num_page == 3:
        return lessons3(request, us, isSave)
    elif num_page == 4:
        return lessons4(request, us, isSave)
    return False


def updateUserModel(isUpdate, us):
    if(isUpdate):
        nextlessons = us.lessonsmax + 1
        us.lessonsmax = nextlessons
        UserModel.objects.all().filter(iduser=us.iduser).update(lessonsmax=nextlessons)

def lessons4(request, us, isSave):
    isRes = True
    res1 = request.POST.get("test[1]")
    res2 = request.POST.get("test[2]")
    res3 = request.POST.get("test[3]")
    res4 = request.POST.get("test[4]")
    res5 = request.POST.get("test[5]")

    if ('0' != res1): return False
    if ('1' != res2): return False
    if ('0' != res3): return False
    if ('2' != res4): return False
    if ('2' != res5): return False

    if(isSave):
        updateUserModel(isRes, us)
    return isRes

def lessons3(request, us, isSave):
    isRes = True
    res1 = request.POST.get("test[1]")
    res2 = request.POST.get("test[2]")
    res3 = request.POST.get("test[3]")
    res4 = request.POST.get("test[4]")
    res5 = request.POST.get("test[5]")

    if ('1' != res1): return False
    if ('2' != res2): return False
    if ('0' != res3): return False
    if ('2' != res4): return False
    if ('0' != res5): return False

    if(isSave):
        updateUserModel(isRes, us)
    return isRes


def lessons2(request, us, isSave):
    isRes = True
    res1 = request.POST.get("test[1]")
    res2 = request.POST.get("test[2]")
    res3 = request.POST.get("test[3]")
    res4 = request.POST.get("test[4]")
    res5 = request.POST.get("test[5]")

    if ('0' != res1): return False
    if ('2' != res2): return False
    if ('1' != res3): return False
    if ('1' != res4): return False
    if ('2' != res5): return False

    if(isSave):
        updateUserModel(isRes, us)
    return isRes

def lessons1(request, us, isSave):
    isRes = True
    res1 = request.POST.get("test[1]")
    res2 = request.POST.get("test[2]")
    res3 = request.POST.get("test[3]")
    res4 = request.POST.get("test[4]")
    res5 = request.POST.get("test[5]")

    if('0' != res1): return False
    if('1' != res2): return False
    if('0' != res3): return False
    if('0' != res4): return False
    if('0' != res5): return False
    if(isSave):
       updateUserModel(isRes, us)

    return isRes
