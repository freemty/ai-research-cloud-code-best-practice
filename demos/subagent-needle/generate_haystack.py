"""
Generate 100 images for the "Needle in a Haystack" subagent demo.
- 99 random noise images
- 1 image with hidden steganographic text embedded in LSB of red channel

The needle image looks identical to noise images visually,
but contains "CLAUDE_CODE_FOUND_ME" encoded in pixel LSBs.
"""

import random
import struct
from pathlib import Path

from PIL import Image
import numpy as np

OUTPUT_DIR = Path(__file__).parent / "haystack"
NUM_IMAGES = 100
IMG_SIZE = (256, 256)
SECRET_MESSAGE = "CLAUDE_CODE_FOUND_ME"


def generate_noise_image(seed: int) -> Image.Image:
    rng = np.random.RandomState(seed)
    pixels = rng.randint(0, 256, (*IMG_SIZE, 3), dtype=np.uint8)
    return Image.fromarray(pixels)


def encode_message_lsb(img: Image.Image, message: str) -> Image.Image:
    """Encode a message into the LSB of the red channel."""
    pixels = np.array(img)

    # Prepend message length as 4-byte header
    msg_bytes = message.encode("utf-8")
    header = struct.pack(">I", len(msg_bytes))
    payload = header + msg_bytes

    bits = []
    for byte in payload:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)

    capacity = IMG_SIZE[0] * IMG_SIZE[1]
    if len(bits) > capacity:
        raise ValueError(f"Message too long: {len(bits)} bits > {capacity} pixels")

    flat_red = pixels[:, :, 0].flatten()
    for i, bit in enumerate(bits):
        flat_red[i] = (flat_red[i] & 0xFE) | bit

    pixels[:, :, 0] = flat_red.reshape(IMG_SIZE)
    return Image.fromarray(pixels)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Decide which index gets the needle
    needle_index = random.randint(0, NUM_IMAGES - 1)

    for i in range(NUM_IMAGES):
        img = generate_noise_image(seed=42000 + i)

        if i == needle_index:
            img = encode_message_lsb(img, SECRET_MESSAGE)
            filename = f"img_{i:03d}.png"
            print(f"[NEEDLE] img_{i:03d}.png  (secret: '{SECRET_MESSAGE}')")
        else:
            filename = f"img_{i:03d}.png"

        img.save(OUTPUT_DIR / filename)

    print(f"\nGenerated {NUM_IMAGES} images in {OUTPUT_DIR}/")
    print(f"Needle hidden at index {needle_index}")

    # Save answer for verification (not shown to Claude)
    (OUTPUT_DIR / ".answer").write_text(f"{needle_index}")


if __name__ == "__main__":
    main()
