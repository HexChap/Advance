import os
from shutil import copy

from PIL import ImageOps, Image

from .utils.get_images import get_images
from .utils.config import paths, border, ROOT_DIR
from .utils.errors import *


class _ImgEditor:
    def __init__(self):
        self.imgs_data = get_images(paths.input_path)

        if self.imgs_data.is_empty():
            raise NoImages(path=paths.input_path)

    def cut_image(self, compress, output_path):
        for path in self.imgs_data.img_paths:
            image = Image.open(path)

            cutted_image = ImageOps.crop(image, border)
            cutted_image.filename = path

            _save_image(cutted_image, compress=compress)

        return self.imgs_data

    def add_logo(self, compress, change_from_center):
        TRANSPARENCY = 50

        watermark = Image.open(
            os.path.join(
                ROOT_DIR,
                "data",
                "logo.png"
            )
        )

        # If the image doesn't have alpha (transparency)
        if watermark.mode != 'RGBA':
            # Adding the transparency parameter to the image
            alpha = Image.new('L', watermark.size, 255)
            watermark.putalpha(alpha)
        paste_mask = watermark.split()[3].point(lambda a: a)

        for path in self.imgs_data.img_paths:
            image = Image.open(path)

            watermark_width = _calc_logo_width(image)
            watermark = _resize_with_proportion(watermark, watermark_width)
            paste_mask = _resize_with_proportion(paste_mask, watermark_width)
            x, y = _calc_logo_coord(image, watermark, change_from_center)

            image.paste(watermark, (x, y), mask=paste_mask)
            image.filename = path

            _save_image(image, compress=compress)

        return self.imgs_data

    def rename_image(self, new_name, output_path):
        for i, path in enumerate(self.imgs_data.img_paths):
            filename = _get_filename(path)
            new_name = str(i) if new_name is None or new_name == "" else new_name

            splitted_filename = filename.split(".")

            old_filename, ext = '.'.join(splitted_filename[:-1]), \
                                        splitted_filename[-1]

            rename_to = f"{new_name}_{i}.{ext}" if new_name else f"{i}.{ext}"

            dst = os.path.join(output_path, rename_to)

            copy(path, dst)

        return self.imgs_data

    def compress_image(self, output_path):
        for path in self.imgs_data.img_paths:
            image = Image.open(path)

            _save_image(image, compress=True)

        return self.imgs_data


class ImgEditor:
    _editor = _ImgEditor()

    def cut_images(self, compress=False, output_path=paths.output_path):
        return self._editor.cut_image(compress=compress, output_path=output_path)

    def add_logo(self, change_from_center=None, compress=False, output_path=paths.output_path):
        return self._editor.add_logo(compress=compress, change_from_center=change_from_center)

    def rename_images(self, new_name=None, output_path=paths.output_path):
        return self._editor.rename_image(new_name=new_name, output_path=output_path)

    def compress_images(self, output_path=paths.output_path):
        self._editor.compress_image(output_path=output_path)


def _save_image(img, compress=False, output_path=paths.output_path):
    filename = _get_filename(img.filename)

    if compress:
        img.save(os.path.join(output_path, filename), optimize=True, quality=50)
    else:   
        img.save(os.path.join(output_path, filename))


def _get_filename(path):
    path = str(path)

    if "\\" in path:
        path.replace("\\", "/")

    return path.split("/")[-1]


def _calc_logo_width(img):
    """Calculate the size of the logo based on the size of the image."""
    return img.size[0] // 4 if img.size[0] > img.size[1] else img.size[0] // 3


def _calc_logo_coord(img, watermark, change_coords):
    x = int((img.size[0] / 2) - (watermark.size[0] / 2))
    y = int((img.size[1] / 2) - (watermark.size[1] / 2))

    if not change_coords == ("" or () or None):
        x += change_coords[0]
        y += change_coords[1]

    return x, y


def _resize_with_proportion(img, basewidth):
    try:
        ratio = (basewidth / float(img.size[0]))
        height = int((float(img.size[1]) * float(ratio)))
        img = img.resize((basewidth, height), Image.ANTIALIAS)
    except:
        raise TypeError("Incorrect argument.")

    return img
