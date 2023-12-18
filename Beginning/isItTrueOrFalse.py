z1= 5
z2= 7
l1= "4"
l2= "9"

if z1 < z2:
    print(z1, "ist kleiner als ", z2, ". Verglichen als Zahl")
else:
    print(z1, "ist nicht kleiner als ", z2, ". Verglichen als Zahl")


if l1 < l2:
    print(l1, "ist kleiner als", l2, ". Verglichen als String")
else:
    print(l1, "ist nicht kleiner ", l2, ". Verglichen als String")

#if z1 < l2:
#    print(z1, "ist kleiner als", l2, ". Verglichen Zahl mit String")
#else:
#    print(z1, "ist nicht kleiner ", l2, ". Verglichen Zahl mit String")

string1 = "Hallo"
string2 = "hallo"
if string1.lower() == string2.lower():
    print("Die Strings sind gleich.")
else:
    print("Die Strings sind ungleich.")