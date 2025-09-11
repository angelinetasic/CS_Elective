students = [ "Shanan", "Zach", "Jam", "Janessa", "Sab" ]

shanan = ("Shanan", 16, 10, "Tau")
zach = ("Zach", 15, 10, "Graviton")
Jam = ("Jam", 15, 10, "Tau")
Janessa = ("Janessa", 15, 10, "Graviton")
Sab = ("Sab", 15, 10, "Tau")

print("Information of Student 3: ")
print("Name: ", Jam[0])
print("Grade: ", Jam[2])
print("Section: ", Jam[3])

grades = {
    "Shanan" : 50,
    "Zach" : 82,
    "Jam" : 75,
    "Janessa" : 96,
    "Sab" : 93,

}

print("Grade of Student 1:", grades["Shanan"])

grades["Shanan"] = 90
print("Updated grade of Shanan:", grades["Shanan"])

grades["Raphy"] = 100
print("New student: Raphy with a grade of", grades["Raphy"])