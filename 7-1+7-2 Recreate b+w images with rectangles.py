#recreate b&w images with ai
from PIL import Image, ImageDraw
import random
original = Image.open("7-1+7-2 images/black_and_white_image_4.jpg")
original = original.convert("1")
original_list = list(original.getdata())
size, size_2 = original.size
art = Image.new("1", (size,size_2), 255)
for k in range(200):
    print(k)
    all_rects = []
    all_colors = []
    all_matrixes = []
    all_similar = []
    for j in range(100):
        add_rect = Image.Image.copy(art)
        house_1 = []
        for i in range(4):
            if i % 2 == 0:
                house_1.append(random.randint(0,size-1))
            else:
                house_1.append(random.randint(0,size_2-1))
        house = ImageDraw.Draw(add_rect)
        rand = random.randint(0,1)
        house.rectangle(house_1,rand*255,rand*255)
        all_rects.append(house_1)
        all_colors.append(rand*255)
        all_matrixes.append(list(add_rect.getdata()))
    #combined = Image.new("1",(size,size_2),1)
    for i in range(len(all_matrixes)):
        similar = 0
        for j in range(len(original_list)):
            if all_matrixes[i][j] == original_list[j]:
                similar += 1
                #combined.putpixel(((j % size),int(j/size)),0)
        all_similar.append(similar)
    maxi = all_similar.index(max(all_similar))
    test = ImageDraw.Draw(art)
    test.rectangle(all_rects[maxi],all_colors[maxi],all_colors[maxi])
art.save("7-1+7-2 images/b+w created image.png")
#combined.save('combined.png')