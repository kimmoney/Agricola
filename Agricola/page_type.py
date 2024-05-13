"""
페이지 리다이렉트를 위한 가상의 URI 타입
"""
from enum import Enum


class PageType(Enum):
    CARD_DISTRIBUTION = 1
    GAME_BOARD = 2
    SCORE_BOARD = 3