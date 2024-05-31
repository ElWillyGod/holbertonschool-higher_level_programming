#!/usr/bin/python3
"""xml"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Create a root element, e.g., <data>.
    Iterate through the dictionary items
    and add them as child elements to the root.
    Write the XML tree to the provided filename using the ET.ElementTree class.
    """

    root = ET.Element('data')

    for i, j in dictionary.items():
        elem = ET.Element(i)
        elem.text = j
        root.append(elem)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Parse the XML file using ET.parse.
    Navigate through the XML elements to reconstruct the dictionary.
    Return the constructed dictionary.
    """

    xmlParse = ET.parse(filename)
    root = xmlParse.getroot()

    dictionary = {}

    for i in root:
        dictionary[i.tag] = i.text

    return dictionary
