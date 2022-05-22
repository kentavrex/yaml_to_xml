import xmlplain

with open('yamlFile.yaml', encoding='utf-8') as infile:
    root = xmlplain.obj_from_yaml(infile)

with open("xmlLibFile.xml", "w", encoding='utf-8') as outfile:
    xmlplain.xml_from_obj(root, outfile)

# без закрывающих </script> выводит. Эта библиотека в большей степени для
# конвертирования xml в yaml, поэтому о недочетах обратного конвертирования написано на сайте документации:
# This will output back the following XML
# (there may be some indentation and/or short empty elements differences w.r.t. the original):

