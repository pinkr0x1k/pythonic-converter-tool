# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:09:47 2020

@author: SAFAK-PC
"""


import pandas as pd

csvfile = pd.read_csv('DEPARTMENTS.csv', sep=';', encoding='utf-8')
jsonfile = open("DEPARTMENTS_csv2new.json", 'w', encoding = 'utf-8')

jsonfile.write('[')

def convert_csv2json(row):
    
    return """
  {
    "university name": "%s",
 	"uType": "%s",
 	"items":  {
 			"faculty": "%s",
     			"department": {
 					"id": "%s",
 					"name": "%s",
 					"lang": "%s",
 					"second": "%s",
 					"period": "%s",
 					"spec": "%s",
 					"quota": "%s",
 					"field": "%s",
 					"last_min_score": "%s",
 					"last_min_order": "%s",
 					"grant": "%s"
				}
		}
  },
""" % (
    row.ÜNİVERSİTE, row.ÜNİVERSİTE_TÜRÜ, row.FAKÜLTE, row.PROGRAM_KODU, row.PROGRAM, row.DİL, row.ÖĞRENİM_TÜRÜ,
    row.ÖĞRENİM_SÜRESİ, row.OKUL_BİRİNCİSİ_KONTENJANI, row.KONTENJAN, row.PUAN_TÜRÜ,
      row.GEÇEN_YIL_MİN_PUAN, row.GEÇEN_YIL_MİN_SIRALAMA, row.BURS)
    

    
jsonfile.write('\n'.join(csvfile.apply(convert_csv2json, axis=1)))
# use the function and create the writer xml object

jsonfile.write(']')

jsonfile.close()




