import os.path

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class ImageProcessor:

    def add_watermark(self, text, filepath=None, pos_x=1, pos_y=1, size=0.1):
        if filepath:
            try:
                with Image.open(filepath) as im:
                    print(filepath, im.format, f"{im.size}x{im.mode}")
                    watermark_image = im.copy()
                    text_height = int(im.size[0] * size)
                    draw = ImageDraw.Draw(watermark_image)
                    font = ImageFont.truetype("arial.ttf", text_height)

                    # Calculate text position aligned
                    text_w = font.getbbox(text)[2]
                    text_h = font.getbbox(text)[3]
                    text_pos_x = im.size[0] * pos_x - (pos_x * text_w)
                    text_pos_y = im.size[1] * pos_y - (pos_y * text_h)

                    draw.text(xy=(text_pos_x, text_pos_y), text=text, fill=(0, 0, 0), font=font)
                    self.save_image(watermark_image, filepath)
            except OSError:
                pass

    @staticmethod
    def save_image(image: Image, filepath: str) -> bool:
        """
        Saves new image in a file with original name plus "watermarked"
        :param image: Watermarked image
        :param filepath: String with original filepath
        :return: True if success in saving file
        """
        try:
            filename = os.path.basename(filepath)
            image.save(f"watermarked_{filename}")
            return True
        except PermissionError:
            return False
