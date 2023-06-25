ListOfNames = ["Hampus", "Edgar", "Ingrid", "Thomas", "Pontus",
               "Dyngrak", "Astrid", "Berit", "Bengan", "Curt",
               "Dennis", "Fiona", "Bob", "Tia", "Johannes",
               "Johanna", "Isabella"]

print("ListOfNames unsorted")
for i in ListOfNames:
    print(i)

print("____________________")
print("ListOfNames sorted alphabetically")
print("____________________")

Alph_sorted_names = sorted(ListOfNames)
for a in Alph_sorted_names:
    print(a)

print("____________________")
print("ListOfNames sorted by length")
print("____________________")

Length_sorted_names = sorted(ListOfNames, key=len, reverse=True)
for l in Length_sorted_names:
    print(l)
