def transpose(text):
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    output_lines = []

    for i in range(max_len):
        chars = []
        for j, line in enumerate(lines):
            if i < len(line):
                chars.append(line[i])
            elif any(i < len(lines[k]) for k in range(j+1, len(lines))):
                chars.append(' ')
        output_lines.append(''.join(chars))

    return '\n'.join(output_lines)