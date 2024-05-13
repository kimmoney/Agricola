"""
건축 자원을 저장하는 엔티티
"""


class Resource:
    def __init__(self):
        self.wood = 0
        self.dirt = 0
        self.reed = 0
        self.rock = 0
        self.grain = 0
        self.vegetable = 0
        self.food = 0
        self.beg_token = 0
        self.first_turn = False
