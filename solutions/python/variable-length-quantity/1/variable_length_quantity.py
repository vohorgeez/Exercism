def encode(numbers):
    result = []
    for number in numbers:
        bytes_ = [number & 0x7F]
        number >>= 7
        while number > 0:
            bytes_.append((number & 0x7F) | 0x80)
            number >>= 7
        result.extend(reversed(bytes_))
    return result


def decode(bytes_):
    result = []
    current = 0
    has_pending = False

    for byte in bytes_:
        has_pending = True
        current = (current << 7) | (byte & 0x7F)
        if byte & 0x80 == 0:  # bit 7 = 0 → dernier byte du nombre
            result.append(current)
            current = 0
            has_pending = False

    if has_pending:
        raise ValueError("incomplete sequence")

    return result