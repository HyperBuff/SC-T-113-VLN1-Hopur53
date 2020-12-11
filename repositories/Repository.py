import csv

class Repository:
    

    def __init__(self):
        self.encoding = 'utf-8'

    # Creates new row in given csv file
    def create(self, filename, fieldnames, row):
        row['id'] = self.generate_id(filename)
        with open(filename, 'a', encoding=self.encoding, newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writerow(row)
        return row

    # Reads csv file, and returns each row as list of dict
    def read(self, filename):
        with open(filename, 'r', encoding=self.encoding, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    
    # Updates row in csv file
    def update(self, filename, fieldnames, identifier, updates):
        rows = self.read(filename)
        modified_rows = []
        for row in rows:
            if row['id'] == str(identifier):
                for key in updates:
                    row[key] = updates[key]
            new_row = row
            modified_rows.append(row)
        self.write(filename, fieldnames, modified_rows)
        return new_row

    # Delete row in csv file
    def delete(self, filename, fieldnames, identifier):
        rows = self.read(filename)
        modified_rows = []
        for row in rows:
            if not row['id'] == str(identifier):
                modified_rows.append(row)
        self.write(filename, fieldnames, modified_rows)
    
    # Writes csv file
    def write(self, filename, fieldnames, rows) -> None:
        with open(filename, 'w', encoding=self.encoding, newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    # Gets unique identifier for created row
    def generate_id(self, filename):

        ids = 'data/ids.csv'
        fieldnames = ['file', 'count']

        rows = self.read(ids)
        for i in range(len(rows)):
            if rows[i]['file'] == filename:
                count = int(rows[i]['count']) + 1
                rows[i]['count'] = str(count)
                self.write(ids, ['file', 'count'], rows)
                return count
        with open(ids, 'a', encoding=self.encoding, newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writerow({'file': filename, 'count': 1})
        return 1
