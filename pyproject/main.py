from fastapi import APIRouter
from api.v1 import translate

router = APIRouter()
router.include_router(translate.router)
