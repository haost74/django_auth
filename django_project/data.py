

def checkRes(request, us):
    if(us.lessonsmax == 1):
       return lessons1(request, us)
    return False



def lessons1(request, us):
    isRes = True
    res1 = request.POST.get("test[1]")
    res2 = request.POST.get("test[2]")
    res3 = request.POST.get("test[3]")
    res4 = request.POST.get("test[4]")
    res5 = request.POST.get("test[5]")

    isRes = '0' == res1
    isRes = '0' == res2
    isRes = '0' == res3
    isRes = '0' == res4
    isRes = '0' == res5

    return isRes
