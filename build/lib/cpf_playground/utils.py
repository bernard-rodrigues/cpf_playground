import re

def is_cpf_format(cpf_string: str) -> bool:
        """
        Checks if a string is in the format XXX.XXX.XXX-XX,
        where each X is a digit from 0 to 9.

        Args:
            cpf_string (str): The string to check.

        Returns:
            bool: True if the string matches the format, False otherwise.
        """
        pattern = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
        return bool(re.match(pattern, cpf_string))