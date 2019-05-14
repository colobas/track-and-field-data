res = "["

x11 = 55.75625
x21 = 476
w1 = 422
h1 = 11.9

x12 = 55.75625
x22 = 476
w2 = 422
h2 = 10.5



for i in range(10):
    y11 = 262.3 + 32*i
    y21 = 275.2 + 32*i

    y12 = 250.65 + 32*i
    y22 = 259.6 + 32*i

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
