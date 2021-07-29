from ArabicOcr import arabicocr


def main(pathImage):
    image_path = pathImage
    out_image = 'out.jpg'
    results = arabicocr.arabic_ocr(image_path, out_image)
    print(results)
    words = []
    for i in range(len(results)):
        word = results[i][1]
        words.append(word)
    with open('file.txt', 'w', encoding='utf-8')as myfile:
        myfile.write(str(words))
    return str(words)
