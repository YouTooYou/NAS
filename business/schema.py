# TODO maak schema class met tree list structure of poppooohh maaak xml dan kan je makkelijk xpathen met global_path jaaaaaa

import xml.etree.ElementTree as ET
from item import Item

file_tree = ET.parse("file.xml")
file_tree.find("." + Item("/").global_path)