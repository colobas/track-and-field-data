res = "["

x11 = 50.575
x21 = 490.13125
w1 = 439.55625
h1 = 9.66875

x12 = 51.31875
x22 = 571.94375
w2 = 520.625
h2 = 17.85

for i in range(14):
    y11 = 268.865625 + 41.5*i
    y21 = 278.534375 + 41.5*i

    y12 = 280.765625 + 41.5*i
    y22 = 298.615625 + 41.5*i

    res += f"""{{
        "page":1,
        "extraction_method":"guess",
        "x1":{x11},
        "x2":{x21},
        "y1":{y11},
        "y2":{y21},
        "width":{w1},
        "height":{h1}
    }},
    {{
        "page":1,
        "extraction_method":"guess",
        "x1":{x12},
        "x2":{x22},
        "y1":{y12},
        "y2":{y22},
        "width":{w2},
        "height":{h2}
    }},"""

res = res[:-1] + "]"

print(res)
