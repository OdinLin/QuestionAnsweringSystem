#!/usr/bin/python
#! -*- coding:utf8 -*-
__author__ = 'odin-lin'

import CandidateAnswerFilter


class CandidateAnswerCanNotInQustionFilter(CandidateAnswerFilter):
    def filter(self, question, candiateanswers):
        questionterms = question.get_terms()
        strs = "对问题分词: "
        for questinterm in questionterms:
            strs += questinterm
            strs += " "

        #答案不能在问题中，去掉
        for candiateanswer in candiateanswers:
            if candiateanswer.get_answer() in questionterms:
                candiateanswers
