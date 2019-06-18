#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description="CLI utility to create tabula "
                                             "templates for Diamond League "
                                             "Race Analysis PDFs")

parser.add_argument("x11", type=float, help="x coordinate of top left corner of first box")
parser.add_argument("x21", type=float, help="x coordinate of top right corner of first box")
parser.add_argument("x12", type=float, help="x coordinate of top left corner of second box")
parser.add_argument("x22", type=float, help="x coordinate of top right corner of second box")

parser.add_argument("w1", type=float, help="width of first box")
parser.add_argument("w2", type=float, help="width of second box")
parser.add_argument("h1", type=float, help="height of first box")
parser.add_argument("h2", type=float, help="height of second box")

parser.add_argument("y11", type=float, help="y coordinate of top left corner of first box")
parser.add_argument("y21", type=float, help="y coordinate of top right corner of first box")
parser.add_argument("y12", type=float, help="y coordinate of top left corner of second box")
parser.add_argument("y22", type=float, help="y coordinate of top right corner of second box")

parser.add_argument("gap", type=float, help="gap between pairs of boxes")
parser.add_argument("N", type=int, help="number of result rows (pairs)")

args = parser.parse_args()

x11 = args.x11
x21 = args.x21
x12 = args.x12
x22 = args.x22

y11 = args.y11
y21 = args.y21
y12 = args.y12
y22 = args.y22

w1 = args.w1
w2 = args.w2
h1 = args.h1
h2 = args.h2

gap = args.gap
N = args.N


res = "["

for i in range(N):
    _y11 = y11 + gap*i
    _y21 = y21 + gap*i

    _y12 = y12 + gap*i
    _y22 = y22 + gap*i

    res += f"""{{
        "page":1,
        "extraction_method":"guess",
        "x1":{x11},
        "x2":{x21},
        "y1":{_y11},
        "y2":{_y21},
        "width":{w1},
        "height":{h1}
    }},
    {{
        "page":1,
        "extraction_method":"guess",
        "x1":{x12},
        "x2":{x22},
        "y1":{_y12},
        "y2":{_y22},
        "width":{w2},
        "height":{h2}
    }},"""

res = res[:-1] + "]"

print(res)
