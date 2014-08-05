#!/usr/bin/python
#! -*- coding:utf8 -*-
__author__ = 'odin-lin'


# 证据由title和snippet组成 对于同一个问题来说，不同的证据的重要性是不一样的，所以证据有分值 证据有多个候选答案
class Evidence(object):
    title = ''
    snippet = ''
    score = 1.0
    candidateAnswerCollection = object