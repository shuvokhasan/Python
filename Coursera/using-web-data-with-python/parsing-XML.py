import xml.etree.ElementTree as ET

data = '''<person>
    <name>Chuck</name>
    <phone type="int1">
        01628884960
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attribute:', tree.find('email').get('hide'))