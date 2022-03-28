import colorgram

rgb_colors = []
colors = colorgram.extract("download.jpeg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

color_list = [(229, 225, 221), (219, 228, 221), (230, 221, 225), (232, 206, 83), (225, 150, 88), (216, 223, 229), (119, 167, 187), (161, 13, 20), (32, 110, 159), (234, 82, 45), (122, 176, 144), (172, 19, 14), (7, 98, 37), (202, 65, 26), (186, 186, 26), (29, 130, 46), (11, 41, 76), (14, 64, 40), (243, 202, 4), (138, 80, 95), (83, 16, 22), (48, 167, 74), (5, 65, 137), (45, 25, 21), (173, 135, 150), (46, 151, 195), (219, 62, 68), (232, 170, 161), (74, 134, 188), (168, 207, 172)]
