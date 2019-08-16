
from PIL import Image
import glob, math

INPUT_PATH = 'input/*.png'
OUTPUT_PATH = 'output.png'

input_sprites = glob.glob(INPUT_PATH)
sample_sprite = Image.open(input_sprites[0])
sprite_width, sprite_height = sample_sprite.size
sprite_count = len(input_sprites)
horizontal_frequency = sprite_height/sprite_height
vertical_frequency = sprite_width/sprite_height
root = math.ceil(sprite_count**.5)
horizontal_count = math.ceil(root * horizontal_frequency)
vertical_count = math.ceil(root * vertical_frequency)

output_image_width = horizontal_count * sprite_width
output_image_height = vertical_count * sprite_height

print('sprite_count: ' + str(sprite_count) + ', horizontal_count: ' + str(horizontal_count) + ', vertical_count: ' + str(vertical_count) + ', horizontal_frequency: ' + str(horizontal_frequency) + ', vertical_frequency: ' + str(vertical_frequency))

output_image = Image.new('RGBA', (output_image_width, output_image_height), color=(0, 0, 0, 0))
for r in range(vertical_count):
    for c in range(horizontal_count):
        index = r * horizontal_count + c
        if index < sprite_count:
            output_image.paste(Image.open(input_sprites[index]), (c * sprite_width, r * sprite_height))

output_image.save(OUTPUT_PATH)