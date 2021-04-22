print("Kiírom a hetes szorzótábla első húsz tagját \n és csillagozom a hárommal oszthatókat.")
cv: int = 0
while cv < 20:
    cv += 1
    b = (7*cv)
    if b % 3 == 0:
        print(str(b)+"*")
    else:
        print(str(b))
