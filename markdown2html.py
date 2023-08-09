#!/usr/bin/python3
"""a script markdown2html.py"""

import sys
import os

def heading_parse(index, lines_read_list):
    """heading tags"""
    count_heading = 0
    list_heading = []
    min_level = 1
    max_level = 6

    while (index < len(lines_read_list)):
        if lines_read_list[index][0] != '#':
            break
        
        data = lines_read_list[index].strip()
        heading_level = len(data) - len(data.lstrip('#'))

        if min_level <= heading_level <= max_level:
            string_to_parsing = data.lstrip("#").strip()
            list_heading.append(f'<h{heading_level}>{string_to_parsing}</h{heading_level}>\n')

        index += 1

    return (index, list_heading)


funtion_parsing = {
    '#': heading_parse,

}


if __name__ == '__main__':
    """a script markdown2html.py"""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    try:
        htmlTagList = []
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        

        with open(input_file, 'r') as f:
            lines_read_list = f.readlines()
            index = 0
            while (index < len(lines_read_list)):
                line = lines_read_list[index].strip()
                first_char = line[0]
                if first_char in funtion_parsing.keys():
                    (index, htmlTag) = funtion_parsing[first_char](index, lines_read_list)
                else:
                    htmlTag = 'parrafo\n'
                    index += 1
                htmlTagList.append(htmlTag)

            print(htmlTagList)

        with open(output_file, 'w') as f:
            for htmlLines in htmlTagList:
                for html_tag in htmlLines:
                    if html_tag:
                        f.write(html_tag)
        
  
        sys.exit(0)
    except FileNotFoundError:
        sys.stderr.write('Missing {}\n'.format(sys.argv[1]))
        sys.exit(1)