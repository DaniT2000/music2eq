import py_midicsv as pm
import csv

upper_notes = []
x = {}
y = {}
# convert MIDI to raw data
def parse_csv():
    csv_string = pm.midi_to_csv("example.midi")
    print(csv_string)


# split data into two groups
def check(input):
    if input in upper_notes:
        return True
    else:
        return False
        
        
def splitter():
    for section in csv_string:
        upper = check(section)
        if upper == True:
            x[]
        else:
            y.append(section)
    
    
# timing fix?
# scale velocity to correct scaling for converter


