import csv

class Repository:
    
    def __init__(self):
        self.encoding = 'utf-8'

    # Creates new row in given csv file
    def _create(self, filename, fieldnames, row) -> dict:
        row['id'] = self.generate_id(filename)
        with open(filename, 'a', encoding=self.encoding, newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writerow(row)
        return row

    # Reads csv file, and returns each row as list of dictionaries
    def _read(self, filename: str) -> list:
        with open(filename, 'r', encoding=self.encoding, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
        
    def _update(self, filename, fieldnames, identifier, updates):
        rows = self._read(filename)
        modified_rows = []
        for row in rows:
            if row['id'] == str(identifier):
                for key in updates:
                    row[key] = updates[key]
            new_row = row
            modified_rows.append(row)
        self.__write(filename, fieldnames, modified_rows)
        return new_row

    def _delete(self, filename, fieldnames, identifier):
        rows = self._read(filename)
        modified_rows = []
        for row in rows:
            if not row['id'] == str(identifier):
                modified_rows.append(row)
        self.__write(filename, fieldnames, modified_rows)
    
    # Writes csv file
    def __write(self, filename, fieldnames, rows) -> None:
        with open(filename, 'w', encoding=self.encoding, newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def generate_id(self, filename):

        ids = 'data/ids.csv'
        fieldnames = ['file', 'count']

        rows = self._read(ids)
        for i in range(len(rows)):
            if rows[i]['file'] == filename:
                count = int(rows[i]['count']) + 1
                rows[i]['count'] = str(count)
                self.__write(ids, ['file', 'count'], rows)
                return count
        with open(ids, 'a', encoding=self.encoding, newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writerow({'file': filename, 'count': 1})
        return 1
