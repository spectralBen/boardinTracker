import csv

class set
    #an entry in the CSV spreadsheet containing the name of the exercise intensity and duration
    def __init__(self, exercise, intensity, reps)
    self.exercise = exercise
    self.intensity = intensity
    self.reps = reps

class day
    #a column in the spreadsheet
    date
    person
    sets = set()


def main():
    with open('hangin n boardin.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for column in csv_reader:
            #add to csv object
            
            
if __name__ == "__main__":
    main()