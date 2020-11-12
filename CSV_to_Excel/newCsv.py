import csv

with open('weight.csv', 'w', newline='') as csvfile:
    fieldnames = ['Datum', 'Systolisch', 'Diastolisch' , 'Puls']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})