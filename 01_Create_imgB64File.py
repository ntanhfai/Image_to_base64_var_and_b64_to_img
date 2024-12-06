import base64
from PIL import Image
import io


def image_to_base64(image_path):
    """Chuyển đổi hình ảnh sang Base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Đường dẫn đến hình ảnh
image_path = r"images\IVIS-logo_brown.png"
imgB64 = image_to_base64(image_path)

# Lưu Base64 vào file Python
with open("imgB64File.py", "w") as file:
    file.write(f"imgB64 = '''{imgB64}'''")
    file.write(
        """
from PIL import Image
import base64
import io

def img_from_base64(base64_string):
    image_data = base64.b64decode(base64_string)
    return Image.open(io.BytesIO(image_data))

imageB64 = img_from_base64(imgB64)
               
               """
    )
