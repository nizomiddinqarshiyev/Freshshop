# dict = {
#     'talaba1': {
#     'name': 'Nizom',
#     'age': 18,
#     'ball': 5,
#     'reyting': 1,
#     },
#
#     'talaba2': {
#     'name': 'Orol',
#     'age': 19,
#     'ball': 3,
#     'reyting': 4,
#     },
#
#     'talaba3': {
#     'name': 'Sarvar',
#     'age': 18,
#     'ball': 4,
#     'reyting': 8,
#     }
# }

# text = """
# 8	Jacket	140	ZW COLLECTION CONTRAST BOMBER JACKET	1
# 15	Head Phones	180	Speciall headphones for your daily use	5
# 9	Shirt	35.95	Slim-fit shirt with a spread collar that buttons on the inside. Long sleeves with buttoned cuffs. Button-up front.	2
# 10	Men's Shirt	35.8	Relaxed fit shirt made of a linen blend. Stand-up collar and long sleeves with buttoned cuffs. Button-up front.	2
# 33	Box	48	Box	2
# 13	Knit wear	180	Sweater made of 20% alpaca and 18% wool. Round neck with long sleeves. Ribbed trims.	5
# 7	Bluze	38	Bluze for girls	15
# 6	KNIT TOP WITH OPEN BACK	120	Top featuring a round neck and long sleeves with cuffs. Open back with tie detail.	8
# 5	Knit wear	180	Sweater made of 20% alpaca and 18% wool. Round neck with long sleeves. Ribbed trims.	10
# 18	STRIPED PANEL DRESS	18.5	STRIPED PANEL DRESS for girls 3-10 years	4
# 14	Sneakers	65	Very good to daily wear	6
# 30	Cream	87	Cream	2
# 29	Brush teeth	13	Brush	4
# 32	Cleaner	17	Cleaner	3
# 25	PUFF SHIRT DRESS	18.9	PUFF SHIRT DRESS	4
# 21	TIE-DYE PLUSH BERMUD SHORT	10	TIE-DYE PLUSH BERMUD SHORT	6
# 20	TIE-DYE PLUSH BERMUD SHORT	10.25	TIE-DYE PLUSH BERMUD SHORT boys	23
# 26	Gray coffe cup	10.3	Gray coffee cup	2
# 28	Towel	18	Towel	6
# 22	TROUSERS PINK	13.2	Trousers for sweet girls	5
# 27	Lamp	180	Lamp	3
# 16	Box	120	Box to your items	6
# 12	Bluze	38	Bluze for girls	3
# 11	Sneakers	115.2	Monochrome sneakers. Contrast rubberised pieces on the upper. Seven-eyelet facing. Chunky sole.	3
# 24	Jacket	10.8	Jacket for you	6
# 34	Pencil	12	Pencil	3
# 23	Silver Shirt 	18.2	Silver shirt using cotton	3
# 37	Faded SkyBlu Denim Jeans	149.45	Mill Oil is an innovative oil filled radiator with the most modern technology. If you are looking for something that can make your interior look awesome, and at the same time give you the pleasant warm feeling during the winter.	5
# 31	Headphones	180	Headphones	5
# 19	CONTRASTS DRESS WITH SLOGAN	9.99	CONTRASTS DRESS WITH SLOGAN 3-8 years	5
# 17	FLORAL SHIRT DRESS	23.14	FLORAL SHIRT DRESS for girls 3-8 years	10
# \."""
#
#
#
# def func(text):
#     arr = text.split('\n')
#     arr1 = []
#     for i in arr:
#         arr1.append(i.split('\t'))
#     return arr1
#
# st = ''
# arr = func(text)
# arr2 = []
# for i in arr:
#     for j in i:
#         st += j + ', '
#     arr2.append(f"({st[:-2]})")
#     print(st)
#     st = ''
#
# for i in  arr2:
#     print(i)
# # print(func(text))

arr = [
    ['Nizom', 18, 5, 1],
    ["O'rol", 19, 3, 8],
    ['Sarvar', 20, 4, 3]
]

b = []

for i in arr:
    b.append(i[3])
b = sorted(b)

for i in b:
    for j in arr:
        if i == j[3]:
            print(j)




















