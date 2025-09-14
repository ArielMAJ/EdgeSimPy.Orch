"""
Root response service class.
"""

from loguru import logger

from src.schemas.root_response import RootResponse


class RootResponseService:
    """
    Root response service class.
    """

    @staticmethod
    async def get_root_response() -> RootResponse:
        """
        Get root response.

        :returns: root response.
        """
        logger.debug("Root endpoint called.")
        return RootResponse(message="Hello World message from the back-end!")
