# -- coding: utf-8 --
"""
Created on Tue Apr 14 23:36:15 2020

@author: SAFAK-PC

"""


import pandas as pd

csv_File = pd.read_csv('DEPARTMENTS.csv', sep=';', encoding='utf-8')
# read the csv file

xml_File = 'DEPARTMENTS_csv2new.xml'
# create the xml file

xmlData = open(xml_File, 'w', encoding='utf-8')
# open a file for writing


xmlData.write('<?xml version="1.0"?>' + "\n")
xmlData.write('<root>' + "\n")
# there must be only one top-level tag


def convert_csv2xml(row):
    return """
    <departments>
         <university uname="%s" utype="%s">
             <item id="%s" faculty="%s">
                 <name lang="%s" edu_style="%s">%s</name>
                 <edu_time>%s</edu_time>
                 <grant>%s</grant>
                 <point_type>%s</point_type>
                 <quota spec="%s">%s</quota>
                 <last_min_score order="%s">%s</last_min_score>
             </item>
        </university>
     </departments> """ % (
    row.ÜNİVERSİTE, row.ÜNİVERSİTE_TÜRÜ, row.PROGRAM_KODU, row.FAKÜLTE, row.DİL, row.ÖĞRENİM_TÜRÜ, row.PROGRAM,
    row.ÖĞRENİM_SÜRESİ, row.BURS, row.PUAN_TÜRÜ, row.OKUL_BİRİNCİSİ_KONTENJANI, row.KONTENJAN,
    row.GEÇEN_YIL_MİN_SIRALAMA, row.GEÇEN_YIL_MİN_PUAN)
    # return the parameters


xmlData.write('\n'.join(csv_File.apply(convert_csv2xml, axis=1)))
# use the function and create the writer xml object

xmlData.write("\n" + '</root>')
# there must be end tag

xmlData.close()
# there must be closed