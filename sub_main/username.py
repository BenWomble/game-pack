import rps


def getuser(i):
    v = rps.user()
    if i in ["n", "N", "no", "No", "NO"]:
        i = "no"
        print("Okay, that is fine. I will call you 'Player' by default. Good luck and have fun.")
#        v = "Player"
    else:
        print("x")
    return getuser(i)
