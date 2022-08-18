from fastapi import APIRouter
from .schemes.translate import SupportedLanguages, translate_text
from .core.config import api_router
from fastapi.responses import RedirectResponse

router = api_router

@router.get("/", include_in_schema=False)
async def root():
    """Root"""
    return RedirectResponse(url="/docs")


@router.post("/translate/")
async def translate_fn(
    source_language: SupportedLanguages,
    destination_language: SupportedLanguages,
    input_text,
):
    """Accept text to translate from source_language to
    destination_language"""
    translated_text = translate_text(source_language, destination_language, input_text)

    return translated_text
