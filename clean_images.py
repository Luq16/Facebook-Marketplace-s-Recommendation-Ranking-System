from PIL import Image
import os

from pandas import wide_to_long

def resize_image(final_size, im):
    size = im.size
    ratio = float(final_size) / max(size)
    new_image_size = tuple([int(x*ratio) for x in size])
    im = im.resize(new_image_size, Image.ANTIALIAS)
    new_im = Image.new("RGB", (final_size, final_size))
    new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
    return new_im

if __name__ == '__main__':
    os.makedirs('modified_images', exist_ok=True) # create new folder
    path = "images/"
    dirs = os.listdir(path)
    final_size = 512
    #loop for all files in directory
    for n, item in enumerate(dirs[:5], 1):
        if not (item.endswith('.png') or item.endswith('.jpg')):
            continue # skip non-image files
        im = Image.open('images/' + item)
        width, height = im.size
        #if width > final_size and height > final_size:
        new_im = resize_image(final_size, im)
        new_im.save(os.path.join('path','modified_images', f'{n}_resized.jpg'))
