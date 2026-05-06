# Modbus RTU CRC-16 Calculator

A lightweight, dependency-free repository containing pure Python and C implementations of the standard Modbus RTU CRC-16 algorithm (Polynomial `0xA001`).

These scripts are designed for embedded developers, system integrators, and field engineers who need a quick way to verify RS485 payload integrity and debug "Ghost Timeouts" or frame errors in industrial networks.

## Usage

### Python
Run the script directly from your terminal to verify your hex frames:
```bash
python modbus_crc.py

C
Easily integrate the ModRTU_CRC() function into your microcontroller (STM32, ESP32, PIC) firmware for real-time edge calculation.

🚀 The Web-based GUI (For Field Testing)
This repo contains the core logic. However, if you are currently on-site, covered in grease, and need a quick way to verify frames on your phone without firing up an IDE or running Python scripts, we hosted a visual version of this calculator here:

👉 Free Modbus CRC & RS485 Signal Analyzer

The web version uses the exact same math but also includes:

Frame structure parsing (Address, Function Code, Data).

RS485 Distance vs. Baud rate safety margin simulation.

Visual alerts for missing 120Ω termination penalties.

Why We Built This
We built this tool internally at Valtoris because 90% of the "hardware failures" our support team deals with turn out to be simple hex math errors or physical layer attenuation. Feel free to use the code in your own SCADA/PLC projects.

Contributions and pull requests are welcome!
