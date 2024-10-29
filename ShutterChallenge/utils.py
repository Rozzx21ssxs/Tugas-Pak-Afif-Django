from PIL import Image
from PIL.ExifTags import TAGS

def extract_exif(file_path):
    exif_data = {}
    try:
        image = Image.open(file_path)
        info = image._getexif()
        if info:
            for tag, value in info.items():
                tag_name = TAGS.get(tag, tag)
                exif_data[tag_name] = value
    except Exception as e:
        print(f"Error reading EXIF data: {e}")
    return exif_data