

def checkRes(request, us):
    if(us.lessonsmax == 1):
       return lessons1(request, us)
    return False


def lessons1(request, us):
    res1 = request.POST.get("test[1]")
    res2 = request.POST.get("test[2]")
    res3 = request.POST.get("test[3]")
    res4 = request.POST.get("test[4]")
    res5 = request.POST.get("test[5]")

    print(res1)
    print(res2)
    print(res3)
    print(res4)
    print(res5)
    return False
