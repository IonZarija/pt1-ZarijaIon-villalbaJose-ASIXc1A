"""

"""
def obt_inp():
    try:
        inp = str(input()).split()
        return inp
    except ValueError:
        return "Error"

def obt_rand(list):
    import random
    a = list[0]
    z = list[-1]
    cen = []
    for x in list:
        if x != 0 or x -1:
            cen.append(list[x])
    random.shuffle(cen)
    palabra = " ".join(cen)
    palabrafinal = a + " " + palabra + " " + z
    return palabrafinal
def obt_ans(list):
    for x in list:
        obt_rand(x)
    frase = frase +

