from xml.dom import minidom
import xml.etree.ElementTree as ET


pnml = ET.Element('pnml')
pnml.set('xmlns', "http://www.pnml.org/version-2009/grammar/pnml")
net = ET.SubElement(pnml, 'net')
net.set('type', 'http://www.pnml.org/version-2009/grammar/ptnet')
net.set('id', 'n-1FF8-E970-0')

name = ET.SubElement(net, 'name')
text = ET.SubElement(name, 'text')
text.text = 'new'

page = ET.SubElement(net, 'page')
page.set('id', 'g-1FF8-F43F-1')


p = ET.SubElement(page, 'place')
p.set('id', 'p-0')
n = ET.SubElement(p, 'name')
text1 = ET.SubElement(n, 'text')
text1.text = 'p0'
marking = ET.SubElement(p, 'initialMarking')
text1 = ET.SubElement(marking, 'text')
text1.text = '1'

c = 0
arc_c = 0

for i in range(20):

    t = ET.SubElement(page, 'transition')
    t.set('id', 't-' + str(c))
    n = ET.SubElement(t, 'name')
    text1 = ET.SubElement(n, 'text')
    text1.text = 't' + str(c)

    p = ET.SubElement(page, 'place')
    p.set('id', 'p-' + str(c + 1))
    n = ET.SubElement(p, 'name')
    text1 = ET.SubElement(n, 'text')
    text1.text = 'p' + str(c + 1)

    a = ET.SubElement(page, 'arc')
    a.set('id', 'a-' + str(arc_c))
    arc_c += 1
    a.set('source', 't-' + str(c))
    a.set('target', 'p-' + str(c))

    a = ET.SubElement(page, 'arc')
    a.set('id', 'a-' + str(arc_c))
    arc_c += 1
    a.set('source', 'p-' + str(c + 1))
    a.set('target', 't-' + str(c))

    c += 1

t = ET.SubElement(page, 'transition')
t.set('id', 't-' + str(c))
n = ET.SubElement(t, 'name')
text1 = ET.SubElement(n, 'text')
text1.text = 't' + str(c)

a = ET.SubElement(page, 'arc')
a.set('id', 'a-' + str(arc_c))
arc_c += 1
a.set('source', 'p-0')
a.set('target', 't-' + str(c))

a = ET.SubElement(page, 'arc')
a.set('id', 'a-' + str(arc_c))
arc_c += 1
a.set('source', 't-' + str(c))
a.set('target', 'p-' + str(c))





# create a new XML file with the results
mydata = ET.tostring(pnml, encoding='unicode')
print(type(mydata))
myfile = open("new.pnml", "w")
myfile.write(mydata)
