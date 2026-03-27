from PIL import Image, ImageFilter, ImageDraw
import random

def glitch_image(input_path, output_path):
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()

    width, height = img.size

    # 🔥 1. Pixel scrambling
    for _ in range(5000):
        x1 = random.randint(0, width - 1)
        y1 = random.randint(0, height - 1)
        x2 = random.randint(0, width - 1)
        y2 = random.randint(0, height - 1)
        pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]

    # 🔥 2. RGB shift
    for _ in range(2000):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        r, g, b = pixels[x, y]
        pixels[x, y] = (b, r, g)

    # 🔥 3. Noise
    for _ in range(3000):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        pixels[x, y] = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    # 🔥 4. Blur
    img = img.filter(ImageFilter.GaussianBlur(radius=1.5))

    # 🟥 5. ADD TEXT HERE (IMPORTANT)
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), "TAMPERED", fill=(255, 0, 0))

    # ✅ Save AFTER everything
    img.save(output_path)
