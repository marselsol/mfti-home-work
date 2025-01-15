#!/usr/bin/env python3
"""
Реализация SHA-256 (FIPS PUB 180-4).
"""

import struct

# Константы, определённые стандартом FIPS PUB 180-4, раздел 4.2.2
K = [
    0x428A2F98, 0x71374491, 0xB5C0FBCF, 0xE9B5DBA5,
    0x3956C25B, 0x59F111F1, 0x923F82A4, 0xAB1C5ED5,
    0xD807AA98, 0x12835B01, 0x243185BE, 0x550C7DC3,
    0x72BE5D74, 0x80DEB1FE, 0x9BDC06A7, 0xC19BF174,
    0xE49B69C1, 0xEFBE4786, 0x0FC19DC6, 0x240CA1CC,
    0x2DE92C6F, 0x4A7484AA, 0x5CB0A9DC, 0x76F988DA,
    0x983E5152, 0xA831C66D, 0xB00327C8, 0xBF597FC7,
    0xC6E00BF3, 0xD5A79147, 0x06CA6351, 0x14292967,
    0x27B70A85, 0x2E1B2138, 0x4D2C6DFC, 0x53380D13,
    0x650A7354, 0x766A0ABB, 0x81C2C92E, 0x92722C85,
    0xA2BFE8A1, 0xA81A664B, 0xC24B8B70, 0xC76C51A3,
    0xD192E819, 0xD6990624, 0xF40E3585, 0x106AA070,
    0x19A4C116, 0x1E376C08, 0x2748774C, 0x34B0BCB5,
    0x391C0CB3, 0x4ED8AA4A, 0x5B9CCA4F, 0x682E6FF3,
    0x748F82EE, 0x78A5636F, 0x84C87814, 0x8CC70208,
    0x90BEFFFA, 0xA4506CEB, 0xBEF9A3F7, 0xC67178F2
]

# Начальные (IV) значения хэша (раздел 5.3.3), каждая константа - 32 бита
INITIAL_HASH = [
    0x6A09E667,
    0xBB67AE85,
    0x3C6EF372,
    0xA54FF53A,
    0x510E527F,
    0x9B05688C,
    0x1F83D9AB,
    0x5BE0CD19
]

def _right_rotate(value, shift):
    """ Битовый сдвиг (ротэйт) вправо на shift бит. """
    return ((value >> shift) | (value << (32 - shift))) & 0xFFFFFFFF

def _sha256_compress(chunk, h):
    """
    Обрабатывает один 512-битный (64-байтовый) chunk
    и обновляет массив h из 8 слов (h0..h7).
    """

    # Преобразуем chunk (64 байта) в массив из 16 слов (big-endian)
    w = list(struct.unpack('>16I', chunk))

    # Расширяем w до 64 слов (W0..W63)
    for i in range(16, 64):
        s0 = _right_rotate(w[i-15], 7) ^ _right_rotate(w[i-15], 18) ^ (w[i-15] >> 3)
        s1 = _right_rotate(w[i-2], 17) ^ _right_rotate(w[i-2], 19) ^ (w[i-2] >> 10)
        w.append((w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF)

    # Инициализируем рабочие переменные a..h
    a, b, c, d, e, f, g, hh = h

    # Главный цикл
    for i in range(64):
        S1 = (_right_rotate(e, 6) ^ _right_rotate(e, 11) ^ _right_rotate(e, 25))
        ch = (e & f) ^ ((~e) & g)
        temp1 = (hh + S1 + ch + K[i] + w[i]) & 0xFFFFFFFF

        S0 = (_right_rotate(a, 2) ^ _right_rotate(a, 13) ^ _right_rotate(a, 22))
        maj = (a & b) ^ (a & c) ^ (b & c)
        temp2 = (S0 + maj) & 0xFFFFFFFF

        hh = g
        g = f
        f = e
        e = (d + temp1) & 0xFFFFFFFF
        d = c
        c = b
        b = a
        a = (temp1 + temp2) & 0xFFFFFFFF

    # Прибавляем полученные значения к текущим (стр.22 FIPS PUB 180-4)
    h[0] = (h[0] + a) & 0xFFFFFFFF
    h[1] = (h[1] + b) & 0xFFFFFFFF
    h[2] = (h[2] + c) & 0xFFFFFFFF
    h[3] = (h[3] + d) & 0xFFFFFFFF
    h[4] = (h[4] + e) & 0xFFFFFFFF
    h[5] = (h[5] + f) & 0xFFFFFFFF
    h[6] = (h[6] + g) & 0xFFFFFFFF
    h[7] = (h[7] + hh) & 0xFFFFFFFF

def sha256(message: bytes) -> bytes:
    """
    Вычисляет SHA-256 хэш для произвольной последовательности байт (message).
    Возвращает 32 байта (256 бит) хэша.
    """

    # 1. Инициализируем h0..h7
    h = INITIAL_HASH[:]

    # 2. Паддинг (добавляем '1', затем нужное число '0', и длину в битах в конце)
    #    см. FIPS PUB 180-4, раздел 4.1.1

    original_length_bits = len(message) * 8

    # Добавляем 0x80 (1000 0000 в бинарном виде)
    message += b'\x80'

    # Добавляем нужное количество нулевых байтов
    # Итоговая длина (mod 512) должна быть 448 (то есть 56 байт) перед добавлением 64-битного размера
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'

    # Добавляем 64-битную длину исходного сообщения (big-endian)
    message += struct.pack('>Q', original_length_bits)

    # 3. Разбиваем message на 512-битные (64-байтные) блоки
    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        _sha256_compress(chunk, h)

    # 4. Формируем итоговый результат (h0..h7 в big-endian)
    #    Каждый элемент h[i] — 32-битное слово
    return struct.pack('>8I', *h)

def sha256_hex_digest(message: bytes) -> str:
    """
    Возвращает SHA-256 в виде шестнадцатеречной строки.
    """
    digest = sha256(message)
    return digest.hex()


def main():
    """
    Пример использования.
    1) Считываем строку от пользователя.
    2) Вычисляем SHA-256.
    3) Выводим хэш в hex-формате.
    4) При изменении хотя бы одного символа хэш меняется радикально.
    """
    print("=== реализация SHA-256 (FIPS PUB 180-4) ===")
    text = input("Введите сообщение: ")
    hash_hex = sha256_hex_digest(text.encode('utf-8'))
    print(f"\nSHA-256 хэш: {hash_hex}")

if __name__ == "__main__":
    main()
