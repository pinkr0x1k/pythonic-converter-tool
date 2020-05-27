# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 04:18:42 2020

@author: SAFAK-PC
"""


import csv
import lxml.etree


with open("DEPARTMENTS_csv2new.xml", 'r', encoding = 'utf-8') as f:
    xml = f.read()
# read the xml file    
       

header = ('uname', 'utype', 'id', 'faculty', 'lang', 'edu_style', 'name', 'edu_time', 'grant', 'point_type', 'spec', 'quota', 'order', 'last_min_score')
# csv file names


with open('DEPARTMENTS_xml2new.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    # create the csv file
    
    writer.writerow(header)
    # write the header names
    
    root = lxml.etree.fromstring(xml)
    
    
    count = 0
    
    for root in root.findall('departments'):
    
        if count > 0:
            
            for university in root.iter('university'):
                uname = university.get('uname')
                utype = university.get('utype')
                
            for item in root.iter('item'):
                id = item.get('id')
                faculty = item.get('faculty')
                
            for name in root.iter('name'):
                lang = name.get('lang')
                edu_style = name.get('edu_style')
                
                name = item.find('name').text
                edu_time = item.find('edu_time').text
                grant = item.find('grant').text
                point_type = item.find('point_type').text
           
            for quota in root.iter('quota'):
                spec = quota.get('spec')
                
                quota = item.find('quota').text
                
            for last_min_score in root.iter('last_min_score'):
                order = last_min_score.get('order')
                
                last_min_score = item.find('last_min_score').text   
 
        
                row = uname, utype, id, faculty, lang, edu_style, name, edu_time, grant, point_type, spec, quota, order, last_min_score
                writer.writerow(row)
                
        count = count + 1





# x = '''
# <?xml version="1.0" encoding="utf-8"?>
# <gpx xmlns:tc2="http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tp1="http://www.garmin.com/xmlschemas/TrackPointExtension/v1" xmlns="http://www.topografix.com/GPX/1/1" version="1.1" creator="TC2 to GPX11 XSLT stylesheet" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd">
# <trk>
#   <name>2013-12-03T21:08:56Z</name>
#   <trkseg>
#     <trkpt lat="45.4852855" lon="-122.6347885">
#       <ele>0.0000000</ele>
#       <time>2013-12-03T21:08:56Z</time>
#     </trkpt>
#     <trkpt lat="45.4852961" lon="-122.6347926">
#       <ele>0.0000000</ele>
#       <time>2013-12-03T21:09:00Z</time>
#     </trkpt>
#     <trkpt lat="45.4852982" lon="-122.6347897">
#       <ele>0.2000000</ele>
#       <time>2013-12-03T21:09:01Z</time>
#     </trkpt>
#   </trkseg>
# </trk>
# </gpx>
# '''





# """!!!"""
# import xml.etree.ElementTree as ET
# import csv
# import re


# with open("DEPARTMENTS.xml", 'r', encoding = 'utf-8') as f:
#     xml = f.read()
    
# root = ET.fromstring(re.sub(r"(<\?xml[^>]+\?>)", r"\1<root>", xml) + "</root>")

# # open a file for writing
# department_data = open('DEPARTMENTSnew.csv', 'w', encoding = 'utf-8')

# # create the csv writer object
# csvwriter = csv.writer(department_data)
# department_head = []

# count = 0



# for member in root.findall('departments'):
 	
#  	if count == 0:
                           
#             university = member.find('university').tag
#             department_head.append(university)
#             utype = member.find('utype').tag
#             department_head.append(utype)
#             faculty = member.find('faculty').tag
#             department_head.append(faculty)
#             item_id = member.find('item_id').tag
#             department_head.append(item_id)
#             program_name = member.find('program_name').tag
#             department_head.append(program_name)
#             lang = member.find('lang').tag
#             department_head.append(lang)
#             edu_style = member.find('edu_style').tag
#             department_head.append(edu_style)
#             grant = member.find('grant').tag
#             department_head.append(grant)
#             edu_time = member.find('edu_time').tag
#             department_head.append(edu_time)
#             point_type = member.find('point_type').tag
#             department_head.append(point_type)
#             quota = member.find('quota').tag
#             department_head.append(quota)
#             first_quota = member.find('first_quota').tag
#             department_head.append(first_quota)
#             last_min_score = member.find('last_min_score').tag
#             department_head.append(last_min_score)
#             last_min_score_point = member.find('last_min_score_point').tag
#             department_head.append(last_min_score_point)
#             csvwriter.writerow(department_head)
#             count = count + 1
            
# for member in root.findall('departments'):
#     department = []
#     if count != 0:
        
#         university = member.find('university').text
#         department.append(university)
#         utype = member.find('utype').text
#         department.append(utype)
#         faculty = member.find('faculty').text
#         department.append(faculty)
#         item_id = member.find('item_id').text
#         department.append(item_id)
#         program_name = member.find('program_name').text
#         department.append(program_name)
#         lang = member.find('lang').text
#         department.append(lang)
#         edu_style = member.find('edu_style').text
#         department.append(edu_style)
#         grant = member.find('grant').text
#         department.append(grant)
#         edu_time = member.find('edu_time').text
#         department.append(edu_time)
#         point_type = member.find('point_type').text
#         department.append(point_type)
#         quota = member.find('quota').text
#         department.append(quota)
#         first_quota = member.find('first_quota').text
#         department.append(first_quota)
#         last_min_score = member.find('last_min_score').text
#         department.append(last_min_score)
#         last_min_score_point = member.find('last_min_score_point').text
#         department.append(last_min_score_point)
#         csvwriter.writerow(department)
#         count = count + 1
         

# department_data.close()

# """!!!"""








# import xml.etree.cElementTree as ET
# import re
# import csv

# # tree = ET.parse("DEPARTMENTS.xml")
# # root = tree.getroot()

# with open("DEPARTMENTS.xml", 'r', encoding = 'utf-8') as f:
#     xml = f.read()
    
# tree = ET.fromstring(re.sub(r"(<\?xml[^>]+\?>)", r"\1<root>", xml) + "</root>")
# # open a file for writing

# department_data = open('DEPARTMENTSData.csv', 'w', encoding = 'utf-8')
# # create the csv writer object

# csvwriter = csv.writer(department_data)
# department_head = []

# count = 0

# for member in tree.findall('departments'):
#  	department = []
    
#  	if count == 0:
                           
#             university = member.find('university').tag
#             department_head.append(university)
#             utype = member.find('utype').tag
#             department_head.append(utype)
#             faculty = member.find('faculty').tag
#             department_head.append(faculty)
#             item_id = member.find('item_id').tag
#             department_head.append(item_id)
#             program_name = member.find('program_name').tag
#             department_head.append(program_name)
#             lang = member.find('lang').tag
#             department_head.append(lang)
#             edu_style = member.find('edu_style').tag
#             department_head.append(edu_style)
#             grant = member.find('grant').tag
#             department_head.append(grant)
#             edu_time = member.find('edu_time').tag
#             department_head.append(edu_time)
#             point_type = member.find('point_type').tag
#             department_head.append(point_type)
#             quota = member.find('quota').tag
#             department_head.append(quota)
#             first_quota = member.find('first_quota').tag
#             department_head.append(first_quota)
#             last_min_score = member.find('last_min_score').tag
#             department_head.append(last_min_score)
#             last_min_score_point = member.find('last_min_score_point').tag
#             department_head.append(last_min_score_point)
#             csvwriter.writerow(department_head)
#             count = count + 1
            


# university = member.find('university').text
# department.append(university)
# utype = member.find('utype').text
# department.append(utype)
# faculty = member.find('faculty').text
# department.append(faculty)
# item_id = member.find('item_id').text
# department.append(item_id)
# program_name = member.find('program_name').text
# department.append(program_name)
# lang = member.find('lang').text
# department.append(lang)
# edu_style = member.find('edu_style').text
# department.append(edu_style)
# grant = member.find('grant').text
# department.append(grant)
# edu_time = member.find('edu_time').text
# department.append(edu_time)
# point_type = member.find('point_type').text
# department.append(point_type)
# quota = member.find('quota').text
# department.append(quota)
# first_quota = member.find('first_quota').text
# department.append(first_quota)
# last_min_score = member.find('last_min_score').text
# department.append(last_min_score)
# last_min_score_point = member.find('last_min_score_point').text
# department.append(last_min_score_point)
# csvwriter.writerow(department)


# department_data.close()



#             university_name = member.find('university_name').tag
#             department_head.append(university_name)
#             utype = member.find('utype').tag
#             department_head.append(utype)
#             item_id = member.find('item_id').tag
#             department_head.append(item_id)
#             faculty = member.find('faculty').tag
#             department_head.append(faculty)
#             name_lang = member.find('name_lang').tag
#             department_head.append(name_lang)
#             edu_style = member.find('edu_style').tag
#             department_head.append(edu_style)
#             name = member.find('name').tag
#             department_head.append(name)
#             edu_time = member.find('edu_time').tag
#             department_head.append(edu_time)
#             grant = member.find('grant').tag
#             department_head.append(grant)
#             point_type = member.find('point_type').tag
#             department_head.append(point_type)
#             quota_spec = member.find('quota_spec').tag
#             department_head.append(quota_spec)
#             quota = member.find('quota').tag
#             department_head.append(quota)
#             last_min_score_order = member.find('last_min_score_order').tag
#             department_head.append(last_min_score_order)
#             last_min_score = member.find('last_min_score').tag
#             department_head.append(last_min_score)
#             csvwriter.writerow(department_head)
#  	count = count + 1
            
        
# university_name = member.find('university_name').text
# department.append(university_name)
# utype = member.find('utype').text
# department.append(utype)
# item_id = member.find('item_id').text
# department.append(item_id)
# faculty = member.find('faculty').text
# department.append(faculty)
# name_lang = member.find('name_lang').text
# department.append(name_lang)
# edu_style = member.find('edu_style').text
# department.append(edu_style)
# name = member.find('name').text
# department.append(name)
# edu_time = member.find('edu_time').text
# department.append(edu_time)
# grant = member.find('grant').text
# department.append(grant)
# point_type = member.find('point_type').text
# department.append(point_type)
# quota_spec = member.find('quota_spec').text
# department.append(quota_spec)
# quota = member.find('quota').text
# department.append(quota)
# last_min_score_order = member.find('last_min_score_order').text
# department.append(last_min_score_order)
# last_min_score = member.find('last_min_score').text
# department.append(last_min_score)
# csvwriter.writerow(department)
    
    
# department_data.close()


#'ÜNİVERSİTE','FAKÜLTE','PROGRAM_KODU','PROGRAM','DİL','ÖĞRENİM_TÜRÜ','BURS','ÖĞRENİM_SÜRESİ','PUAN_TÜRÜ','KONTENJAN','OKUL_BİRİNCİSİ_KONTENJANI','GEÇEN_YIL_MİN_SIRALAMA','GEÇEN_YIL_MİN_PUAN'


    #  <utype="%s">
    # <university>%s</university>
    # <faculty>%s</faculty>
    # <item_id>%s</item_id>
    # <program_name>%s</program_name>
    # <lang>%s</lang>
    # <edu_style>%s</edu_style>
    # <grant>%s</grant>
    # <edu_time>%s</edu_time>
    # <point_type>%s</point_type>
    # <quota>%s</quota>
    # <first_quota>%s</first_quota>
    # <last_min_score>%s</last_min_score>
    # <last_min_score_point>%s</last_min_score_point>
    # </utype>   


        
