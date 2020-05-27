# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:32:28 2020

@author: SAFAK-PC
"""

import lxml.etree


def xmlValidator(xml_filepath, xsd_filepath):
    
    xml_file = lxml.etree.parse(xml_filepath)
    xsd_validator = lxml.etree.XMLSchema(file = xsd_filepath)
    is_valid = xsd_validator.validate(xml_file)
    if(is_valid):
        return print("[+] XML file verified")
    else:
        return print("[-] XML file could not be verified")
    
    xmlValidator("DEPARTMENTS.xml", "DEPARTMENTS.xsd")