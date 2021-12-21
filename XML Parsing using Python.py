import xml.etree.ElementTree as ET

tree = ET.parse(r"C:\Users\geniu\Desktop\untitled.xml")     ## Element tree object
root = tree.getroot()

#root = ET.fromstring(country_data_as_string) 
#fromstring() parses XML from a string directly into an Element, which is the root element of the parsed tree.


print(root.tag, root.attrib, root[0].attrib,root[0].get('id'))

## tag -> returns current tag name
## attrib ->    returns attribute of current element in dictionary format i.e in key-value pair
## get('id) ->     returns value of attribute of current element
print(root[0].tag, root[0].attrib)
print(root[0][1].tag, root[0][1].attrib, root[0][1].text)

for child in root:
    print("sub node:-{}".format(child.tag),"\t\t","sub node attribute:-{}".format(child.attrib))

for child in root[0]:
    print("sub node:-{}".format(child.tag),"\t\t","sub node attribute:-{}".format(child.attrib))

for i in root.findall('book'):
    author = i.find('author').text
    price = i.find('price').text
    print(author,price)


for i in root.iter('genre'):        ## Iterating over all 'genre' tags
    a = str(i.text)+'New description added'     ## Edited description
    i.text = a
    i.set('updated','Yes')      ## added a new attribute named as 'updated' having value 'yes'

tree.write('sample.xml')        ## new xml created as per hanges made on prev. xml file

## Adding subelements:

ET.SubElement(root[0],'Sale')       ## root[0] is the element under which we want to add new sub-element with name 'Sale'
for x in root.iter('Sale'):
    x.text = str('Sale is good')


tree.write('sample2.xml')


## Adding new element:-

ele = ET.Element("book")
ele.text = "New element added"
root.append(ele)

tree.write('sample7.xml')


## Deleting any attribute from xml:-

## Lets delete attribute 'id' under 'book' subelement

root[0].attrib.pop('id')    ## Provide name of the attribute you want to remove under root[0] sub-element 

tree.write('sample3.xml')

#                   OR

#for i in tree.findall('book'):
#    del(i.attrib['id'])
#tree.write('sample7.xml')


## Deleting any element/ subelement from xml:-

root[0].remove(root[0][0])
tree.write('sample4.xml')

## Cleaning all subelement under an element in xml:-

root[0].clear()
tree.write('sample5.xml')

## Finding element by selecting nodes by path as:-
find_ele = root.find(".//book[@id='bk103']")

print(find_ele.text)