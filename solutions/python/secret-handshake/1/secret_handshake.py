def commands(binary_str):
    instructions = [
        'reverse',
        'jump',
        'close your eyes',
        'double blink',
        'wink'
        ]
    secret_check = []
    for i in range(4, -1, -1):
        if binary_str[i] == '1':
            secret_check.append(instructions[i])
    if secret_check == []:
        return []
    if secret_check[-1] == 'reverse':
        secret_check.pop()
        secret_check.reverse()
    return secret_check