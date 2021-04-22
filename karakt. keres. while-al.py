print("Az általad beírt karaktersorozatban megkeresem az általad beírt karaktert...")
a: str = ""
b: str = ""
while b in a:
    a = input("Add meg egy karaktersorozatot:")
    b = input("Add meg azt a betűt, amit megkeressek:")
    if b not in a:
        a: str = ""
        b: str = ""
        continue
    elif b in a:
        print("Te az " + b + " betűt kerested, és az ebbe a szóba benne van.")
        break
