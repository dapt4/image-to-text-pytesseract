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
    save_path = 'results/' + file_name + '.txt'
    with open(save_path, 'w') as f:
        f.write(text)
        print('File saved to: ' + save_path)

def get_img(url, file_name):
    res = get(url, stream=True)
    if res.status_code == 200:
        download_path = 'images/' + file_name
        with open(download_path, 'wb') as f:
            copyfileobj(res.raw, f)


def main():
    option = input('Do you have the image in the images folder? (y/n): ')
    path = 'images/'
    if (option == 'y' or option == 'Y'):
        path += input("Enter the image name: ")
    else:
        url = input("Enter the image url: ")
        file_name = input("Enter the image name: ")
        get_img(url, file_name)
        path += file_name
    text = image_to_text(path)
    save_to_file(path, text)

if __name__ == "__main__":
    main()
