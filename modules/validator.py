import re


def validate(name: str) -> bool:
    """Проверка логина на валидность"""
    name = ''.join(name.split())
    valid_pattern = re.compile(r"^[а-яА-ЯёЁa-zA-Z0-9]+$", re.I)
    return not bool(valid_pattern.match(name))
