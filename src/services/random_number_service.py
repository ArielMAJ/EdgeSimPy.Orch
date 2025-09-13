"""
Random number service class.
"""

import random

from loguru import logger

from src.schemas.random_number import RandomResponse


class RandomResponseService:
    """
    Random number service class.
    """

    @staticmethod
    async def get_random_number() -> RandomResponse:
        """
        Get random number.

        :returns: random number.
        """
        logger.debug("Random number endpoint called.")
        random_number = random.randint(1, 100)
        return RandomResponse(message=random_number)
