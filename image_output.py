from PIL import Image, ImageDraw
import csv

def draw(file,name):
    width = 28 # ширина изображения
    height = 28 # высота изображения
    image = Image.new("L", (width,height)) # режим - изображения в оттенках серого
    draw = ImageDraw.Draw(image)
    with open(file, encoding='utf-8') as r_file:
       # Создаем объект reader, указываем символ-разделитель ","
       file_reader = csv.reader(r_file, delimiter = ",")
       count = 0 # Счетчик для подсчета количества строк и вывода заголовков столбцов
       j = 0 #для названия файлов
       for line in file_reader:
           if count == 0:
               print(f'Файл содержит столбцы: {", ".join(line)}')
           else:
               pix = line
               i = 0 
               label = pix[i] # нулевой символ в массиве - метка изображения
               i = 1
               for x in range(width):
                   for y in range(height):
                       pix[i] = int(pix[i])
                       pix[i] = 255 - pix[i] # 0 - background(white), 255 - foreground (black)
                       draw.point((y,x), (pix[i])) # рисуем по точкам
                       i = i + 1
               j = str(j)
               image.save(f"F:\\fashion_mnist\\{name}\\{label}\\img{j}.jpg", "JPEG")
               j = int(j)
               j = j + 1
           count += 1
    r_file.close()

print("Введите расположение файла обучающей выборки: ")
file1 = input()
print("Введите расположение файла тестовой выборки: ")
file2 = input()
draw(file1,"train")
draw(file2,"test")