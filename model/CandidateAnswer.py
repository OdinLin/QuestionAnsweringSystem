#!/usr/bin/python
#! -*- coding:utf8 -*-
__author__ = 'odin-lin'


class CandidateAnswer(object):
    answer = ''
    score = 1.0

    def __init__(self):
        pass

    def get_answer(self):
        return self.answer

    def set_answer(self, answer):
        self.answer = answer

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def add_score(self, score):
        self.score += score

    def __ne__(self, other):
        return self.score != other.score

    def __eq__(self, other):
        return self.score == other.score

    def __gt__(self, other):
        return self.score > other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __lt__(self, other):
        return self.score < other.score

    def __le__(self, other):
        return self.score <= other.score

    def __hash__(self):
        return hash(self.answer)