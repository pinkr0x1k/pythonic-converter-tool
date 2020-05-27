# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 04:18:42 2020

@author: SAFAK-PC
"""
import sys
import lxml
import csv
import json
import pandas as pd
import xml.etree.ElementTree as elmtree

from lxml import etree
from collections import defaultdict


class xml2json:
    """A XML TO JSON class"""

    def _init_(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        return print(
            "[*] Processing XML to JSON operation :\n\t [op_info] <" + input_file + "> -> <" + output_file + ">")

    def xmlParser(self, t):
        data = {t.tag: {} if t.attrib else None}  # initilize data if there is child node and attr
        children = list(t)  ## if tag has childeren hold in the list
        if children:  ## then if childeren has exist map has
            dd = defaultdict(
                list)  ## Added to branch to dict structure, so we will able to map if any there is another child
            for dc in map(self.xmlParser,
                          children):  # walk in the child an fuction call itself again for same process. until one branch remains
                for key, value in dc.items():  ## After the json array is end, each key value added to key dict
                    dd[key].append(value)
            data = {t.tag: {key: value[0] if len(value) == 1 else value
                            for key, value in dd.items()}}
        if t.attrib:  ## if there is attribute key updated with attribute KEY VALUE pairs
            data[t.tag].update(('-' + key, value)
                               for key, value in t.attrib.items())
        if t.text:  ## if the node has not parent or parent is empty, add to list. so if it is json object
            text = t.text.strip()
            if children or t.attrib:
                if text:
                    data[t.tag]['#text'] = text
            else:
                data[t.tag] = text
        return data

    ## get the root of xml if root is exist call the xmlParser func
    def tojson(self, data):
        try:
            root = elmtree.ElementTree(elmtree.fromstring(data)).getroot()
        except:
            return print("[-] Please check your xml structure!")
        if root:
            return self.xmlParser(root)


    ## this fuction is a service for parse xml to json
    def xml2json(self):
        xml_file = lxml.etree.parse(self.input_file)
        parsed_xml = lxml.etree.tostring(xml_file)
        with open(self.output_file, 'w') as json_file:
             json.dump(json.dumps(self.tojson(parsed_xml), indent=2), json_file)

        return print("[+] Process is complated")


class json2xml:
    """A XML TO JSON class"""

    def _init_(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        return print(
            "[*] Processing JSON to XML operation :\n\t [op_info] <" + input_file + "> -> <" + output_file + ">")

    def jsonParser(self, t, factory=elmtree.Element):
        attribs = {}  ## intital attr
        text = None
        tail = None
        sublist = []  ## inital array holder
        tag = list(t.keys())  ## All of keys added to list
        if len(tag) != 1:  ## tag has element
            raise ValueError("[-] Please check your json structure!: %s" % tag)
        tag = tag[0]  ## if has element, get root and value
        value = t[tag]
        if isinstance(value, dict):  ## if key has child either array nor not value check recursively
            for k, v in list(value.items()):  ## Then, all key and value pairs assigned for appended to xml item
                if k[:1] == "-":  ## if its attr
                    attribs[k[1:]] = v
                elif k == "#text":  ## if it is text
                    text = v
                elif k == "#tail":
                    tail = v
                elif isinstance(v, list):
                    for v2 in v:
                        sublist.append(self.jsonParser({k: v2}, factory=factory))
                else:
                    sublist.append(self.jsonParser({k: v}, factory=factory))
        else:  ##  assign all key and value pairs
            text = value
        e = factory(tag, attribs)
        for sub in sublist:
            e.append(sub)
        e.text = text
        e.tail = tail
        return e

    def servXml(self, json_data, factory=elmtree.Element):
        if not isinstance(json_data, dict):
            json_data = json.loads(json_data).decode('utf-8')  ## get json then parse it

        parsed_json = self.jsonParser(json_data, factory)
        parsed_data = elmtree.tostring(parsed_json)  ## getted json data toString for writing xml document
        return  parsed_data

    def json2xml(self):
        with open(self.input_file, 'r') as f:
                xx = self.servXml(json.load(f))
                o_file = open(self.output_file, "w")
                o_file.write(xx.decode('utf-8'))
                
        return print("[+] Process is complated")


class xml2csv:
    """A XML TO CSV class"""

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        return print(
            "[*] Processing XML to CSV operation :\n\t [op_info] <" + input_file + "> -> <" + output_file + ">")

    def xml2csv(self):
        
        ## read the xml file
        with open(self.input_file, 'r', encoding='utf-8') as f:
            xml = f.read()

        ## csv file names
        header = (
            'uname', 'utype', 'id', 'faculty', 'lang', 'edu_style', 'name', 'edu_time', 'grant', 'point_type', 'spec',
            'quota', 'order', 'last_min_score')

        with open(self.output_file, 'w', encoding='utf-8') as f:

            writer = csv.writer(f)  ## create the csv file
            writer.writerow(header)  ## write the header names

            root = lxml.etree.fromstring(xml)
            count = 0

            for root in root.findall('departments'):  ## take the all roots

                ##iteration controll
                if count > 0:  ## is it iterate?

                    for university in root.iter('university'):   ## then, main tags on the loop for the iterable
                        uname = university.get('uname')
                        utype = university.get('utype')

                    for item in root.iter('item'):  ## same process above
                        id = item.get('id')
                        faculty = item.get('faculty')

                    for name in root.iter('name'):
                        lang = name.get('lang')
                        edu_style = name.get('edu_style')

                        name = item.find('name').text   ## item 'text field' find
                        edu_time = item.find('edu_time').text
                        grant = item.find('grant').text
                        point_type = item.find('point_type').text

                    for quota in root.iter('quota'):
                        spec = quota.get('spec')

                        quota = item.find('quota').text

                    for last_min_score in root.iter('last_min_score'):
                        order = last_min_score.get('order')

                        last_min_score = item.find('last_min_score').text

                        # finally, added row all items
                        row = uname, utype, id, faculty, lang, edu_style, name, edu_time, grant, point_type, spec, quota, order, last_min_score
                        writer.writerow(row)  # then write row to file

                count = count + 1   ##for the other loop

        return print("[+] Process is complated")


class csv2xml:
    """A CSV TO XML class"""

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        return print(
            "[*] Processing CSV to XML operation :\n\t [op_info] <" + input_file + "> -> <" + output_file + ">")

    def createXml(self, row):   ##column fields turn row by row
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
            </departments> """ % (   ##each row will be inside tag by tag
            row.ÜNİVERSİTE, row.ÜNİVERSİTE_TÜRÜ, row.PROGRAM_KODU, row.FAKÜLTE, row.DİL, row.ÖĞRENİM_TÜRÜ, row.PROGRAM,
            row.ÖĞRENİM_SÜRESİ, row.BURS, row.PUAN_TÜRÜ, row.OKUL_BİRİNCİSİ_KONTENJANI, row.KONTENJAN,
            row.GEÇEN_YIL_MİN_SIRALAMA, row.GEÇEN_YIL_MİN_PUAN)

    def csv2xml(self):
        
        ## read the csv file
        csv_File = pd.read_csv(self.input_file, sep=';', encoding='utf-8')

        ## create the xml file
        xml_File = self.output_file

        ## open a file for writing
        xmlData = open(xml_File, 'w', encoding='utf-8')

        ## there must be only one top-level tag
        xmlData.write('<?xml version="1.0"?>' + "\n")
        xmlData.write('<root>' + "\n")

        ## use the function and create the writer xml object
        xmlData.write('\n'.join(csv_File.apply(self.createXml, axis=1)))

        ## there must be end tag
        xmlData.write("\n" + '</root>')

        ## file there must be closed
        xmlData.close()
        
        return print("[+] Process is complated")


class csv2json:
    """A CSV TO JSON class"""

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        return print(
            "[*] Processing CSV to JSON operation :\n\t [op_info] <" + input_file + "> -> <" + output_file + ">")

    def createJson(self, row):   ##column fields turn row by row
        return """{
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
    			}, """ % (   ##each row will be inside tag by tag
            row.ÜNİVERSİTE, row.ÜNİVERSİTE_TÜRÜ, row.FAKÜLTE, row.PROGRAM_KODU, row.PROGRAM, row.DİL, row.ÖĞRENİM_TÜRÜ,
            row.ÖĞRENİM_SÜRESİ, row.OKUL_BİRİNCİSİ_KONTENJANI, row.KONTENJAN, row.PUAN_TÜRÜ,
            row.GEÇEN_YIL_MİN_PUAN, row.GEÇEN_YIL_MİN_SIRALAMA, row.BURS)

    def csv2json(self):
        csv_file = pd.read_csv(self.input_file, sep=';', encoding='utf-8')
        json_file = open(self.output_file, 'w', encoding='utf-8')

        json_file.write('[')
        json_file.write(
            '\n'.join(csv_file.apply(self.createJson, axis=1)))  ## use the function and create the writer xml object
        json_file.write(']')
        json_file.close()
        
        return print("[+] Process is complated")

class json2csv:
    """A JSON TO CSV class"""

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        return print(
            "[*] Processing JSON to CSV operation :\n\t [op_info] <" + input_file + "> -> <" + output_file + ">")

    def json2csv(self):
        with open(self.input_file) as json_file:   ## open the json file
            json_f = json.load(json_file, encoding='utf-8')   ## read the json file
            f = csv.writer(open(self.output_file, "w", encoding='utf-8'))   ## create the csv file
            f.writerow(
                ["university name", "uType", "faculty", "id", "name", "land", "second", "period", "spec", "quota",
                 "field", "last_min_score", "last_min_order", "grant"])

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

            return print("[+] Process is complated")


class validateXsd:

    def __init__(self, xml_file, xsd_file):
        self.xml_file = xml_file
        self.xsd_file = xsd_file

    def xmlValidator(self, xml_file, xsd_file):

        xml_file = lxml.etree.parse(self.xml_file)   ## xml file parsing
        xsd_validator = lxml.etree.XMLSchema(file=self.xsd_file)
        is_valid = xsd_validator.validate(xml_file)  ##is it validated?

        if (is_valid):
            return print("[+] XML file verified")
        else:
            return print("[-] XML file could not be verified")


def main():
    if (len(sys.argv) < 3):
        return print("Check your arguments !!!")

    print(sys.argv)
    input_file = ''
    output_file = ''

    ##checking operations
    if (sys.argv[3] == '1'):
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        op = csv2xml(input_file, output_file)
        op.csv2xml()
    elif (sys.argv[3] == '2'):
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        op = xml2csv(input_file, output_file)
        op.xml2csv()
    elif (sys.argv[3] == '3'):
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        op = xml2json(input_file, output_file)
        op.xml2json()
    elif (sys.argv[3] == '4'):
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        op = json2xml(input_file, output_file)
        op.json2xml()
    elif (sys.argv[3] == '5'):
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        op = csv2json(input_file, output_file)
        op.csv2json()
    elif (sys.argv[3] == '6'):
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        op = json2csv(input_file, output_file)
        op.json2csv()
    elif (sys.argv[3] == '7'):
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        op = validateXsd(input_file, output_file)
        op.xmlValidator()
    else:
        print(
            "Please enter valid argumets and operation \m/ \n\t" + "input : <" + sys.argv[1] + "> output: <" + sys.argv[
                2] + ">")

if __name__ == "__main__":
    main()
