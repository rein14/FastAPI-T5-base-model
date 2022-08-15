from enum import Enum

from transformers import T5ForConditionalGeneration, T5Tokenizer

tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small", return_dict=True)


def translate_text(source, destination, input_texts):
    """Translate text base defined source to destination"""
    input_ids = tokenizer(
        f"translate {source} to {destination}: {input_texts}", return_tensors="pt"
    ).input_ids
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return decoded


class SupportedLanguages(str, Enum):
    """Languages supported by the t5-base model"""

    ENGLISH = "English"
    FRENCH = "French"
    ROMANIAN = "Romanian"
    GERMAN = "German"

