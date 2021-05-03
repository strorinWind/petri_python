from funcs import *

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


p = add_place(page, 0)
marking = ET.SubElement(p, 'initialMarking')
text1 = ET.SubElement(marking, 'text')
text1.text = '1'

c = 0
arc_c = 0

for i in range(20):
    add_transition(page, c)
    add_place(page, c + 1)

    add_arc(page, arc_c, 't-' + str(c), 'p-' + str(c))
    arc_c += 1
    add_arc(page, arc_c, 'p-' + str(c + 1), 't-' + str(c))
    arc_c += 1

    c += 1

add_transition(page, c)

add_arc(page, arc_c, 'p-0', 't-' + str(c))
arc_c += 1
add_arc(page, arc_c, 't-' + str(c), 'p-' + str(c))
arc_c += 1

c += 1
center_id = c
add_place(page, center_id)
add_arc(page, arc_c, 't-0', 'p-' + str(center_id))
arc_c += 1
add_transition(page, c)
add_arc(page, arc_c, 'p-' + str(center_id), 't-' + str(center_id))
arc_c += 1
c += 1

with_marking = c
p = add_place(page, with_marking)
marking = ET.SubElement(p, 'initialMarking')
text1 = ET.SubElement(marking, 'text')
text1.text = '1'

add_arc(page, arc_c, 'p-' + str(c), 't-' + str(center_id))
arc_c += 1
c += 1
add_place(page, c)
add_arc(page, arc_c, 't-' + str(center_id), 'p-' + str(c))
arc_c += 1
add_transition(page, c)
add_arc(page, arc_c, 'p-' + str(c), 't-' + str(c))
arc_c += 1

add_arc(page, arc_c, 't-' + str(c), 'p-' + str(with_marking))


# create a new XML file with the results
mydata = ET.tostring(pnml, encoding='unicode')
print(type(mydata))
myfile = open("new.pnml", "w")
myfile.write(mydata)
