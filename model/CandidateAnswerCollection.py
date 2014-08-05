#!/usr/bin/python
#! -*- coding:utf8 -*-
__author__ = 'odin-lin'


# 候选答案集合 包含多个候选答案
class CandidateAnswerCollection(object):
    candidateAnswers = set()

    def __init__(self):
        pass

    def is_empty(self):
        return len(self.candidateAnswers) == 0

    # 获取所有候选答案
    def get_all_candidate_answer(self):
        return sorted(list(self.candidateAnswers), reverse=True)

    def show_all(self):
        candidate_answer_list = self.get_all_candidate_answer()
        for candidateAnswer in candidate_answer_list:
            print candidateAnswer.answer + candidateAnswer.score

    # 按CandidateAnswer的分值排序，返回topN
    def get_topn_candidateanswer(self, topn):
        candidate_answer_list = self.get_all_candidate_answer()
        length = len(candidate_answer_list)
        if topn > length:
            topn = length

        return sorted(candidate_answer_list, reverse=True)[0:topn-1]

    def show_topn(self):
        candidate_answer_list = self.get_topn_candidateanswer()
        for candidateAnswer in candidate_answer_list:
            print candidateAnswer.answer + candidateAnswer.score

    def add_answer(self, candidate_answer):
        if candidate_answer not in self.candidateAnswers:
            self.candidateAnswers.add(candidate_answer)

    def remove_answer(self, candidate_answer):
        if candidate_answer in self.candidateAnswers:
            self.candidateAnswers.remove(candidate_answer)