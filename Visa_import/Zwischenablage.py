"""  date = row["Buchungsdatum"]
                merchand = row["Händler (Name, Stadt & Land)"]
                amo = row["Betrag in Euro"]
            
           #Ab hier werden die Lines an das CSV File angehängt
            with open (dstFileName , 'a+', newline='') as csvfile:
                fieldnames = ['Date', 'Dealer','Amount']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'Date': date, 'Dealer': merchand, 'Amount': amo})
        csvdatei.close()
        csvfile.close()
    logging.info("CSV Datei erfolgreich geschrieben!!!") """