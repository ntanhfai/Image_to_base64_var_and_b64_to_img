from PIL import Image
import base64
import io
from imgB64File import imgB64


def img_from_base64(base64_string):
    #Chuyển Base64 về hình ảnh PIL. 
    image_data = base64.b64decode(base64_string)
    return Image.open(io.BytesIO(image_data))


# Sử dụng biến imgB64 từ file imgB64File
image = img_from_base64(imgB64)

# Hiển thị hình ảnh
image.show()

# Lưu hình ảnh (nếu cần)
image.save("output_image.png")
