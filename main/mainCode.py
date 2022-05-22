class YamlToXmlConverter:
    def primitiveYamlListCreator(self):
        space = ' '
        primitive_list = []
        with open('yamlFile.yaml', encoding='utf-8') as yaml:
            for line in yaml:
                upgrated = line.split(space)
                nested_counter = upgrated.count('')
                if nested_counter != 0:
                    primitive_list.append(nested_counter)
                    primitive_list += list(filter(lambda a: a != '', upgrated))  # replace all spaces to their number
                else:
                    primitive_list += upgrated
        return primitive_list
        # now we have the list with string items and the integer number of spaces

    def valuesGlue(self):
        # below we will join values together
        buffer, yaml_list, space = '', [], ' '
        primitive_list = self.primitiveYamlListCreator()
        for line in primitive_list:
            if type(line) != int and ':' not in line:
                if '-' not in line or (buffer != '' and type(buffer[-1]) != int):  # here we check the position of '-'
                    buffer = buffer + str(line) + space
                if '\n' in line or line == primitive_list[-1]:
                    if line == primitive_list[-1]:
                        buffer = buffer[:-1] + '\n'
                        yaml_list.append(buffer)
                    else:
                        yaml_list.append(buffer[:-1])  # add the value list without last rudimentary space
                    buffer = ''
            else:
                yaml_list.append(line)
        # print(yaml_list)
        return yaml_list

    # the yaml-massive is ready and below will be filling the xml file
    def correctSpaceYamlList(self):
        yaml_list = self.valuesGlue()
        for ind in range(len(yaml_list)):
            item = yaml_list[ind]
            if type(item) != int and str(item).count(':') != 1 and '\n' in item:
                if ind + 1 != len(yaml_list) and yaml_list[ind + 1] != '-':
                    yaml_list[ind + 1] -= 2
        yaml_list += [2]  # for to have the last 2-nested clothing tag
        return yaml_list

    # above we trimmed our spaces but the yaml-type spaces will be made below

    # all below vars ind functions will be used in nearest while-cycle
    def nearest_tag_for_closing_finder(self, some_list, cycle_iterator, current_yaml_list):
        yaml_list = current_yaml_list
        some_list = some_list
        i = cycle_iterator
        iterator = i
        while True:
            tmpItem = yaml_list[iterator]
            if type(tmpItem) == int:
                iterator -= 1
                continue
            elif ":\n" in tmpItem:
                if yaml_list[iterator - 1] in some_list:
                    break
            iterator -= 1
        tag = '/' + str(tmpItem)
        return tag, tmpItem

    def yamlList(self):
        yaml_list = self.correctSpaceYamlList()
        step = 2  # exactly that much spaces has one step in yaml format file
        was_more_than_4 = False
        was_more_than_2 = False
        i = 0  # iterator for while_cycle
        # below we use while-cycle instead of more understandable for-cycle because
        # yaml_list dynamically changes during the cycle
        while i != len(yaml_list) - 1:
            i += 1
            this_item = yaml_list[i]
            low_degree, mid_degree, deep_degree = step, step * 2, step * 3
            if type(this_item) == int:
                if this_item >= deep_degree:
                    yaml_list[i] -= step
                    was_more_than_4 = True
                    was_more_than_2 = True
                elif this_item == mid_degree:
                    if was_more_than_4:
                        was_more_than_4 = False
                        tag = self.nearest_tag_for_closing_finder([step, step * 2, step * 3, step * 4], i, yaml_list)[0]
                        yaml_list = yaml_list[:i + 1] + [tag] + yaml_list[i:]
                        # with this above slices we save the spaces before and after closing tag
                    was_more_than_2 = True
                elif this_item == low_degree:
                    if was_more_than_2:
                        was_more_than_2 = False
                        tag, tmpItem = self.nearest_tag_for_closing_finder([step], i, yaml_list)
                        # below cycle is for checking right neighbors if they are not only space-numbers
                        is_righterAnythingExeptSpaceNumbers = False
                        for right_k in yaml_list[i:]:
                            if type(right_k) != int:
                                is_righterAnythingExeptSpaceNumbers = True
                        if is_righterAnythingExeptSpaceNumbers:
                            yaml_list = yaml_list[:i + 1] + [tag] + [yaml_list[i]] + \
                                        [str(tmpItem)] + [yaml_list[i]] + yaml_list[i:]
                        # with this slices we save the spaces before and after tag ([yaml_list[i]] - number-space)
                        else:
                            yaml_list = yaml_list[:i + 1] + [tag]
        return yaml_list

    # now we have yuml_list with yaml-type spaces! below we will add closing tags and we can print all!

    # the yaml_list is all ready and it's just stayed to print this list by some rules!
    def mainPart(self):
        xml = open('xmlMainFile.xml', 'w', encoding='utf-8')
        yaml_list = self.yamlList()
        space = ' '
        xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        for ind in range(len(yaml_list)):
            item = yaml_list[ind]
            if item == '\n':
                xml.write(item)
            elif item == '<subject>':
                xml.write(item + '\n')
            else:
                if ind in {0, len(yaml_list) - 1}:  # check if item hasn't got prev_ and next_
                    if ind == 0:
                        prev_item = None
                    else:
                        next_item = None
                else:
                    prev_item, next_item = yaml_list[ind - 1], yaml_list[ind + 1]

                if type(item) == int:
                    xml.write(space * item)
                elif item == '-':
                    continue
                else:
                    # below we put < > to keys
                    if str(item).count(':') == 1:
                        if '\n' in item:
                            clear_word = item[:-2]  # without ':\n'
                            xml.write("<" + clear_word + ">" + '\n')
                        else:
                            xml.write("<" + str(item[:-1]) + ">")  # without ':'
                    else:
                        if '\n' in item:
                            clear_word = item[:-1]  # without '\n'
                            # xmlLine with closing tag with previous key
                            if item == yaml_list[-1]:
                                xmlLine = str(clear_word) + "</" + str(yaml_list[ind - 1][:-1]) + ">"
                            else:
                                xmlLine = str(clear_word) + "</" + str(prev_item[:-1]) + ">"
                            xml.write(xmlLine + '\n')
                        else:
                            xml.write(str(item))

        xml.write('</' + yaml_list[0][:-2] + '>')  # global file clothing tag
        xml.close()


my_converter = YamlToXmlConverter()
my_converter.mainPart()
