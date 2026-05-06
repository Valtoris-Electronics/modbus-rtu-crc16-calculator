# Modbus RTU CRC-16 Calculator

A lightweight, dependency-free repository containing pure Python and C implementations of the standard Modbus RTU CRC-16 algorithm (Polynomial `0xA001`).

These scripts are designed for embedded developers, system integrators, and field engineers who need a quick way to verify RS485 payload integrity and debug "Ghost Timeouts" or frame errors in industrial networks.

## Usage

### Python
Run the script directly from your terminal to verify your hex frames:
```bash
python modbus_crc.py
