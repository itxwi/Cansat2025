import json


class Enums:
    def __init__(self):
        """
        Decimal as the 126th value, ~ reserved for negative sign.
        """
        self.chart_92 = {i - 32: chr(i) for i in range(33, 125)}  # Base 92
        self.chart_92[0] = '~'  # Reserve '~' for negative sign
        self.reverse_chart_92 = {v: k for k, v in self.chart_92.items()}

    def generate_92(self):
        return {i - 32: chr(i) for i in range(33, 125)}

    def convert_92(self, num):
        """
        Converts a number (integer or float) to base 92.
        Handles negative numbers by prefixing with '~'.
        """
        if not isinstance(num, (int, float)):
            raise TypeError("Input must be an integer or a float.")

        is_negative = num < 0
        num = abs(num)

        integer_part = int(num)
        fractional_part = num - integer_part

        integer_base92 = self._int_to_base92(integer_part)
        fractional_base92 = self._fraction_to_base92(fractional_part, precision=5)

        result = integer_base92
        if fractional_base92:
            result += "." + fractional_base92

        if is_negative:
            result = "~" + result

        return result

    def _int_to_base92(self, n):
        """
        Converts the integer part of a number to base 92.
        """
        if n == 0:
            return self.chart_92[1]  # '0' in chart_92
        digits = []
        while n > 0:
            remainder = n % 92
            digits.insert(0, self.chart_92[remainder])
            n //= 92
        return "".join(digits)

    def _fraction_to_base92(self, fraction, precision=5):
        """
        Converts the fractional part of a number to base 92.
        """
        if fraction == 0:
            return ""
        digits = []
        for _ in range(precision):
            fraction *= 92
            integer_part = int(fraction)
            digits.append(self.chart_92[integer_part])
            fraction -= integer_part
            if fraction == 0:
                break
        return "".join(digits)

    def convert_from_92(self, base92_str):
        """
        Converts a base 92 encoded string back to its original number.
        Handles negative numbers prefixed with '~'.
        """
        if not isinstance(base92_str, str):
            raise TypeError("Input must be a string.")

        if base92_str.startswith("~"):
            is_negative = True
            base92_str = base92_str[1:]
        else:
            is_negative = False

        if not all(char in self.reverse_chart_92 or char == '.' for char in base92_str):
            raise ValueError("Invalid characters in base-92 string.")

        if base92_str.count('.') > 1:
            raise ValueError("Invalid base-92 string: multiple decimal points.")

        integer_part_str, *fractional_part_list = base92_str.split('.')
        fractional_part_str = fractional_part_list[0] if fractional_part_list else ""

        integer_value = 0
        for char in integer_part_str:
            integer_value = integer_value * 92 + self.reverse_chart_92[char]

        fractional_value = 0
        for i, char in enumerate(fractional_part_str):
            fractional_value += self.reverse_chart_92[char] * (92 ** -(i + 1))

        result = integer_value + fractional_value
        return -result if is_negative else result