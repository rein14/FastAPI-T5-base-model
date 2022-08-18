from enum import Enum


class SupportedLanguages(str, Enum):
    """Languages supported by the t5-base model"""

    ENGLISH = "English"
    FRENCH = "French"
    ROMANIAN = "Romanian"
    GERMAN = "German"
