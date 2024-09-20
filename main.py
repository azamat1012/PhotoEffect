from PIL import Image
from pathlib import Path

# relevant directory to photos
current_dir = Path(__file__).parent
file_path_photo_old = current_dir/'old_img'/'monro.jpg'
file_path_photo_new = current_dir/'new_img'


img = Image.open(file_path_photo_old)

red, blue, green = img.split()

red_left = img.crop((50, 0, red.width, red.height))
red_middle = img.crop((25, 0, red.width - 25, red.height))
red_offset = Image.blend(red_left, red_middle, 0.5).convert("L")

blue_right = img.crop((0, 0, blue.width-50, blue.height))
blue_middle = img.crop((25, 0, blue.width-25, blue.height))
blue_offset = Image.blend(blue_right, blue_middle, 0.5).convert("L")

green_resized = green.resize(red_left.size)

# Checking the mode/ It must be "L"
print(f"red_offset mode: {red_offset.mode}")
print(f"green_resized mode: {green_resized.mode}")
print(f"blue_offset mode: {blue_offset.mode}")

final_image = Image.merge("RGB", (red_offset, blue_offset, green_resized))

final_image.thumbnail((80, 80))

final_image.save(f"{file_path_photo_new}/final_image.jpg")
