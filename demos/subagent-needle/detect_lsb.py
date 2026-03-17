"""
LSB steganography detector — checks if an image has a hidden message
encoded in the least significant bits of the red channel.

Usage:
    python detect_lsb.py <image_path>
    python detect_lsb.py haystack/img_042.png

Exit code 0 + prints message if found, exit code 1 if not found.
"""

import struct
import sys
from pathlib import Path

import numpy as np
from PIL import Image


def extract_lsb_message(image_path: str) -> str | None:
    """Extract a potential LSB-encoded message from the red channel."""
    img = Image.open(image_path)
    pixels = np.array(img)
    flat_red = pixels[:, :, 0].flatten()

    # Extract LSBs
    lsbs = flat_red & 1

    # Read 4-byte header (32 bits) for message length
    if len(lsbs) < 32:
        return None

    header_bits = lsbs[:32]
    header_bytes = bytearray()
    for i in range(0, 32, 8):
        byte = 0
        for j in range(8):
            byte = (byte << 1) | int(header_bits[i + j])
        header_bytes.append(byte)

    msg_len = struct.unpack(">I", bytes(header_bytes))[0]

    # Sanity check: message length should be reasonable
    if msg_len == 0 or msg_len > 1000:
        return None

    total_bits = 32 + msg_len * 8
    if total_bits > len(lsbs):
        return None

    # Extract message bytes
    msg_bits = lsbs[32:total_bits]
    msg_bytes = bytearray()
    for i in range(0, len(msg_bits), 8):
        byte = 0
        for j in range(8):
            byte = (byte << 1) | int(msg_bits[i + j])
        msg_bytes.append(byte)

    try:
        decoded = bytes(msg_bytes).decode("utf-8")
        # Verify it's printable ASCII/UTF-8
        if all(c.isprintable() for c in decoded):
            return decoded
        return None
    except (UnicodeDecodeError, ValueError):
        return None


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <image_path>")
        sys.exit(2)

    image_path = sys.argv[1]
    if not Path(image_path).exists():
        print(f"File not found: {image_path}")
        sys.exit(2)

    result = extract_lsb_message(image_path)
    if result:
        print(f"FOUND: {result}")
        sys.exit(0)
    else:
        print("CLEAN")
        sys.exit(1)


if __name__ == "__main__":
    main()
