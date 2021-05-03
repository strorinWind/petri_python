
import xml.etree.ElementTree as ET


def add_place(parent, id_num):
    p = ET.SubElement(parent, 'place')
    p.set('id', 'p-' + str(id_num))
    n = ET.SubElement(p, 'name')
    text1 = ET.SubElement(n, 'text')
    text1.text = 'p' + str(id_num)
    return p


def add_transition(parent, id_num):
    t = ET.SubElement(parent, 'transition')
    t.set('id', 't-' + str(id_num))
    n = ET.SubElement(t, 'name')
    text1 = ET.SubElement(n, 'text')
    text1.text = 't' + str(id_num)
    return t


def add_arc(parent, id_num, source, target):
    a = ET.SubElement(parent, 'arc')
    a.set('id', 'a-' + str(id_num))
    a.set('source', source)
    a.set('target', target)
    pass
