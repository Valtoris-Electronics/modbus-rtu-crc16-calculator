#include <stdio.h>
#include <stdint.h>

/**
 * @brief Calculates Modbus RTU CRC-16
 * @param buf Pointer to the byte array
 * @param len Length of the byte array
 * @return 16-bit CRC value
 */
uint16_t ModRTU_CRC(uint8_t buf[], int len) {
    uint16_t crc = 0xFFFF;
    for (int pos = 0; pos < len; pos++) {
        crc ^= (uint16_t)buf[pos];    // XOR byte into least sig. byte of crc
        for (int i = 8; i != 0; i--) { // Loop over each bit
            if ((crc & 0x0001) != 0) { // If the LSB is set
                crc >>= 1;             // Shift right and XOR 0xA001
                crc ^= 0xA001;
            } else {                   // Else LSB is not set
                crc >>= 1;             // Just shift right
            }
        }
    }
    return crc;
}

int main() {
    // Example Frame: 01 03 00 00 00 02
    uint8_t test_frame[] = {0x01, 0x03, 0x00, 0x00, 0x00, 0x02};
    int length = sizeof(test_frame) / sizeof(test_frame[0]);
    
    uint16_t crc_res = ModRTU_CRC(test_frame, length);
    
    // Print in little-endian format (Low Byte first, then High Byte)
    printf("CRC-16 Result: %02X %02X\n", crc_res & 0xFF, crc_res >> 8);
    
    return 0;
}
