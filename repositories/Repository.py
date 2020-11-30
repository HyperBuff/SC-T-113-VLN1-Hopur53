import csv

class Repository:

    def __init__(self):
        self.encoding = 'utf-8'

    # Reads csv file, and returns each row as list of dictionaries
    def read(self, filename: str) -> list:
        with open(filename, 'r', encoding=self.encoding, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    
    # Writes csv file
    def write(self, filename, fieldnames, rows) -> None:
        with open(filename, 'w', encoding=self.encoding, newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    
    # Adds row to csv file
    def append(self, filename, fieldnames, row) -> dict:
        with open(filename, 'a', encoding=self.encoding, newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writerow(row)
        return row

