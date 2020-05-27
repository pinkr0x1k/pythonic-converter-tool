# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 03:40:47 2020

@author: SAFAK-PC
"""


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