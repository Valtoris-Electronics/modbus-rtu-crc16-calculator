#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Modbus RTU CRC-16 Calculator
A lightweight script for calculating Modbus RTU CRC-16 checksums.
Perfect for debugging RS485 frames on the fly.
"""

def calculate_modbus_crc16(data_hex_string: str) -> str:
    """
    Calculates the Modbus RTU CRC-16 for a given hex string.
    """
    # Clean up the input string (remove spaces)
    hex_str = data_hex_string.replace(" ", "")
    data_bytes = bytes.fromhex(hex_str)
    
    crc = 0xFFFF
    for byte in data_bytes:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
                
    # Swap bytes for Modbus little-endian format
    crc_bytes = crc.to_bytes(2, byteorder='little')
    return crc_bytes.hex().upper()

if __name__ == "__main__":
    # Example: Read Holding Registers (Node 01, Func 03, Addr 0000, 2 Regs)
    test_frame = "01 03 00 00 00 02"
    crc_result = calculate_modbus_crc16(test_frame)
    
    print(f"Original Frame: {test_frame}")
    print(f"CRC-16 Result : {crc_result[:2]} {crc_result[2:]}")
    print(f"Full Frame    : {test_frame} {crc_result[:2]} {crc_result[2:]}")
