"""
마술사 직업 카드
"""
from behavior.job.job_interface import JobInterface


class Magician(JobInterface):
    def canUse(self):
        pass

    def execute(self):
        pass

    def log(self):
        pass

    def putDown(self):
        pass