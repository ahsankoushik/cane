from image_read import take_photo
from image_read import image_read


take_photo.capture_write('test.jpg')
print(image_read.extract_text('test.jpg'))

