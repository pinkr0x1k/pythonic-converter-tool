
# -- coding: utf-8 --
"""
Created on Wed Apr 15 04:18:42 2020

@author: SAFAK-PC
"""
import re
import csv
import json
import xml.etree.ElementTree as elmtree

import lxml
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
