#!/usr/bin/env python
# -*- coding=UTF-8 -*-

a = {'log_id': 7816679558872603572, 'direction': 0, 'words_result_num': 3, 'words_result': [{'vertexes_location': [{'y': 48, 'x': 93}, {'y': 48, 'x': 168}, {'y': 69, 'x': 168}, {'y': 69, 'x': 93}], 'probability': {'variance': 0.0, 'average': 0.999781, 'min': 0.999749}, 'chars': [{'char': '议', 'location': {'width': 14, 'top': 48, 'left': 93, 'height': 23}}, {'char': '发', 'location': {'width': 14, 'top': 48, 'left': 154, 'height': 23}}], 'min_finegrained_vertexes_location': [{'y': 48, 'x': 93}, {'y': 48, 'x': 168}, {'y': 69, 'x': 168}, {'y': 69, 'x': 93}], 'finegrained_vertexes_location': [{'y': 48, 'x': 93}, {'y': 48, 'x': 115}, {'y': 48, 'x': 138}, {'y': 48, 'x': 161}, {'y': 48, 'x': 168}, {'y': 59, 'x': 168}, {'y': 69, 'x': 168}, {'y': 69, 'x': 145}, {'y': 69, 'x': 122}, {'y': 69, 'x': 100}, {'y': 69, 'x': 93}, {'y': 58, 'x': 93}], 'location': {'width': 76, 'top': 48, 'left': 93, 'height': 23}, 'words': '议发'}, {'vertexes_location': [{'y': 88, 'x': 74}, {'y': 88, 'x': 144}, {'y': 109, 'x': 144}, {'y': 109, 'x': 74}], 'probability': {'variance': 0.000718, 'average': 0.940434, 'min': 0.913637}, 'chars': [{'char': '暴', 'location': {'width': 15, 'top': 88, 'left': 108, 'height': 23}}, {'char': '寡', 'location': {'width': 14, 'top': 88, 'left': 129, 'height': 23}}], 'min_finegrained_vertexes_location': [{'y': 88, 'x': 74}, {'y': 88, 'x': 144}, {'y': 109, 'x': 144}, {'y': 109, 'x': 74}], 'finegrained_vertexes_location': [{'y': 88, 'x': 74}, {'y': 88, 'x': 97}, {'y': 88, 'x': 120}, {'y': 88, 'x': 142}, {'y': 88, 'x': 144}, {'y': 99, 'x': 144}, {'y': 109, 'x': 144}, {'y': 109, 'x': 122}, {'y': 109, 'x': 99}, {'y': 109, 'x': 76}, {'y': 109, 'x': 74}, {'y': 98, 'x': 74}], 'location': {'width': 72, 'top': 88, 'left': 74, 'height': 23}, 'words': '暴寡'}, {'vertexes_location': [{'y': 158, 'x': 95}, {'y': 158, 'x': 165}, {'y': 180, 'x': 165}, {'y': 180, 'x': 95}], 'probability': {'variance': 0.084168, 'average': 0.585507, 'min': 0.366177}, 'chars': [{'char': '惹', 'location': {'width': 14, 'top': 158, 'left': 130, 'height': 24}}], 'min_finegrained_vertexes_location': [{'y': 158, 'x': 95}, {'y': 158, 'x': 165}, {'y': 180, 'x': 165}, {'y': 180, 'x': 95}], 'finegrained_vertexes_location': [{'y': 158, 'x': 95}, {'y': 158, 'x': 118}, {'y': 158, 'x': 142}, {'y': 158, 'x': 165}, {'y': 170, 'x': 165}, {'y': 180, 'x': 165}, {'y': 180, 'x': 142}, {'y': 180, 'x': 118}, {'y': 180, 'x': 95}, {'y': 169, 'x': 95}], 'location': {'width': 71, 'top': 158, 'left': 95, 'height': 24}, 'words': '惹'}]}


import jsonpath
result = jsonpath.jsonpath(a,"$..chars")
for each in result:
    for i in each:
        char = i.get("char")
        if char == "寡":
            location = i.get("location")
            x = location.get("left")
            y = location.get("top")
            print(x,y)
