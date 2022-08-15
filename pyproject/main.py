from fastapi import FastAPI,status
from fastapi.responses import RedirectResponse
from .core import config
from .schemes import translate

app = FastAPI()
app.include_router(config.router)


@config.router.get("/", include_in_schema=False)
async def root():
    """Root"""
    return RedirectResponse(url="/docs")


@app.post("/translate/")
async def translate_fn(
    source_language: translate.SupportedLanguages,
    destination_language: translate.SupportedLanguages,
    input_text,
):
    """Accept text to translate from source_language to
     destination_language"""
    translated_text = translate.translate_text( source_language, 
                                    destination_language,\
                                    input_text
                                    )
 
    return translated_text