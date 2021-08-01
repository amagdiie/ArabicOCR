from os.path import dirname, join
from ArabicOcr import arabicocr
import tempfile
import io


def main(content):
    content = bytes(content)
    content_file = io.BytesIO(content)
    filename = ""
    with tempfile.NamedTemporaryFile() as temp_file:
        temp_file.write(content)
        filename = temp_file.name
    results = arabicocr.arabic_ocr(str(filename), 'out.jpg')
    print(results)
    words = []
    for i in range(len(results)):
        word = results[i][1]
        words.append(word)
    return str(words)
