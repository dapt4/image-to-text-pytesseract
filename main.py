import pytesseract
from PIL import Image
from requests import get
from shutil import copyfileobj

def image_to_text(path):
    image = Image.open(path)
    text = pytesseract.image_to_string(image)
    return text

def save_to_file(path, text):
    file_name = path.split('/')[1].split('.')[0]
    save_path = 'results/' + filen_name + '.txt'
    with open(save_path)

def main():
    option = input('Do you have the image in the images folder? (y/n): ')
    path = 'images/'
    if (option == 'y' or option == 'Y'):
        path += input("Enter the image name: ")
    else:
        url = input("Enter the image url: ")
        file_name = input("Enter the image name: ")
        res = get(url, stream=True)
        if res.status_code == 200:
            with open(file_name, 'wb') as f:
                copyfileobj(res.raw, f)
                path += file_name
    text = image_to_text(path)
    save_to_file(path, text)

if __name__ == "__main__":
    main()
