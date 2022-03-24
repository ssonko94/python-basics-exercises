import csv
import module_01


my_wedding = module_01.my_wedding

with open("my_school.csv", "w+") as my_wedding:
    filewriter = csv.writer(my_wedding, delimiter=",")
    filewriter.writerow(["Department", "Personnel"])
    filewriter.writerow(["Headmaster", "Bakka Male"])
    filewriter.writerow(["Physics", "John Okiror"])
    filewriter.writerow(["Math", "Akullu Flavia"])
    filewriter.writerow(["English", "Nakayiza Annet"])
    filewriter.writerow(["Chemistry", "Chemutai Matthew"])
    filewriter.writerow(["Biology", "Mulondo Chris"])
    filewriter.writerow(["Geography", "Ssentamu Christopher"])
    filewriter.writerow(["History", "Walugembe Simon"])
    filewriter.writerow(["Agriculture", "Mugabi Timothy"])
    filewriter.writerow(["Techinical Drawing", "Sabiti Nicholas"])
