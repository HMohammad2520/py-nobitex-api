# nobitex_api\_utils.py
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

__all__ = [
    'logger',
]