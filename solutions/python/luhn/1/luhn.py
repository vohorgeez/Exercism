class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        stripped = self.card_num.replace(" ", "")
        if not stripped.isdigit():
            return False
        if len(stripped) <= 1:
            return False
        even = len(stripped) % 2 == 0
        if not even:
            stripped = "0" + stripped
        to_sum = []
        for i in range(len(stripped)):
            if i % 2 == 0:
                to_add = int(stripped[i]) * 2
                if to_add > 9:
                    to_add -= 9
                to_sum.append(to_add)
            else:
                to_sum.append(int(stripped[i]))
        final_sum = sum(to_sum)
        return final_sum % 10 == 0