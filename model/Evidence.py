#!/usr/bin/python
#! -*- coding:utf8 -*-
__author__ = 'odin-lin'

import parser.WordParser

# 证据由title和snippet组成 对于同一个问题来说，不同的证据的重要性是不一样的，所以证据有分值 证据有多个候选答案


class Evidence(object):
    title = ''
    snippet = ''
    score = 1.0
    candidateAnswerCollection = object

    def get_title_terms(self):
        result = list()
        terms = WordParser.parse(self.title)
        for term in terms:
            result.append(term.getname())

        return result

    def get_snippet_terms(self):
        result = list()
        terms = WordParser.parse(self.snippet)
        for term in terms:
            result.append(term.getname())

        return result

     #对证据进行分词
     #
     #return 分词结果
    def get_terms(self):
        result = list()
        terms = WordParser.parse(self.title + self.snippet)
        for term in terms:
            result.append(term.getname())

        return result

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_snippet(self):
        return self.snippet

    def set_snippet(self, snippet):
        self.snippet = snippet

    def get_score(self):
        return self.score

    def add_score(self, score):
        self.score += score

    def get_candidate_answer_collection(self):
        return self.candidateAnswerCollection

    def set_candidate_answer_collection(self, candidateanswercollection):
        self.candidateAnswerCollection = candidateanswercollection