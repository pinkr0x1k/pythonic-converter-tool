# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:08:10 2020

@author: SAFAK-PC
"""

import csv
import json

def json2csv(self):
    with open(self.input_file) as json_file:   ## open the json file
     json_f = json.load(json_file, encoding='utf-8')   ## read the json file
     f = csv.writer(open(self.output_file, "w", encoding='utf-8'))   ## create the csv file
     f.writerow(["university name", "uType", "faculty", "id", "name", "land", "second", "period", "spec", "quota", "field", "last_min_score", "last_min_order", "grant"])
                    
     for json_f in json_f:   ##row by row writing 
                f.writerow([json_f["university name"],
                            json_f["uType"],
                            json_f["items"]["faculty"],
                            json_f["items"]["department"]["id"],
                            json_f["items"]["department"]["name"],
                            json_f["items"]["department"]["lang"],
                            json_f["items"]["department"]["second"],
                            json_f["items"]["department"]["period"],
                            json_f["items"]["department"]["spec"],
                            json_f["items"]["department"]["quota"],
                            json_f["items"]["department"]["field"],
                            json_f["items"]["department"]["last_min_score"],
                            json_f["items"]["department"]["last_min_order"],
                            json_f["items"]["department"]["grant"]])












