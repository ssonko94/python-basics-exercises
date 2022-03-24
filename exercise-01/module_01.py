import csv

with open("my_wedding.csv", "w+") as my_wedding:
    filewriter = csv.writer(my_wedding, delimiter=",")
    filewriter.writerow(["wedding contributors", "items", "price"])
    filewriter.writerow(["Odongo Morris", "wedding cake", "2m"])
    filewriter.writerow(["Kanyike Steven", "Music", "1m"])
    filewriter.writerow(["Ali Hamis", "chicken", "600k"])
