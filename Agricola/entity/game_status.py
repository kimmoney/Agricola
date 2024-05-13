"""
게임 전체의 진행 상태를 저장하는 클래스
"""

class GameStatus:
    def __init__(self):
        self.now_round = 0
        self.round_card_order = [[i for i in range(0, 4)],
                                 [i for i in range(4, 7)],
                                 [i for i in range(7, 9)],
                                 [i for i in range(9, 11)],
                                 [i for i in range(11, 13)],
                                 [i for i in range(13, 14)]]

