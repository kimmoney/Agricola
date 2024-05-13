"""
현재 해당 플레이어가 사용할 수 있는 카드들에 대한 정보
"""


class OwnCard:
    def __init__(self):
        self.handSubCard = []
        self.handJobCard = []
        self.putSubCard = []
        self.putJobCard = []
        self.putMainCard = []