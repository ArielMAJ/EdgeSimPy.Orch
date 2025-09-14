from fastapi.routing import APIRouter

from src.entrypoints import monitoring, random_response, root_response

router = APIRouter()
router.include_router(monitoring.router, tags=["Monitoring"])
router.include_router(
    random_response.router, prefix="/random_number", tags=["Random Number"]
)
router.include_router(root_response.router, tags=["Root Response"])

__all__ = ["router"]
