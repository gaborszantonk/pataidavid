print("A program egy karaktersorozatban kicseréli az f betűket ph-ra, \n mint például Szofoklész ---- Szophoklész")
print("---------")
a = input("Kezdjük, itt add meg a karaktersorozatot! :")
b = "ph"
for cv in range(len(a)):
    print(a.replace("f", b))
    break
