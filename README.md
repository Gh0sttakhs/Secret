# Homoglyph Encryption/Decryption Tool

A Python-based utility designed to encrypt and decrypt messages by leveraging homoglyphs between the Greek and English character sets. 

## Overview
This tool performs character substitution using visually similar characters (homoglyphs) across different Unicode blocks. It provides a simple yet effective way to obfuscate text, ensuring that the encrypted output appears visually identical or very similar to standard text while being fundamentally different at the byte level.

## Features
- **Bidirectional Conversion:** Seamlessly encrypt plain text and decrypt homoglyph-encoded messages.
- **Cross-Alphabet Support:** Utilizes both Greek and English character mappings for substitution.
- **Lightweight & Fast:** Pure Python implementation with no external dependencies required.

## Tech Stack
- **Language:** Python 3.x

## Usage
*(Add your specific execution commands here, e.g.)*
```bash
# Example encryption command
python homoglyph_tool.py --encrypt "Your message here"

# Example decryption command
python homoglyph_tool.py --decrypt "Yοur mеssagе hеrе"
