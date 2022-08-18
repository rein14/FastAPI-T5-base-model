from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from transformers import T5ForConditionalGeneration, T5Tokenizer

from .core.config import api_router
from .schemes.translate import SupportedLanguages

tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small", return_dict=True)


app = FastAPI()


@app.get("/", include_in_schema=False)
async def root():
    """Root"""
    return RedirectResponse(url="/docs")


@api_router.post(
    "/translate",
    status_code=status.HTTP_200_OK,
    response_description="Sucess",
)
async def translate_fn(
    source_language: SupportedLanguages,
    destination_language: SupportedLanguages,
    input_text,
):
    """Translate text base defined source to destination"""
    input_ids = tokenizer(
        f"translate {source_language} to {destination_language}: {input_text}", return_tensors="pt"
    ).input_ids
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return decoded

app.include_router(api_router)
