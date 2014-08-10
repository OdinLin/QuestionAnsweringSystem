#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'odin-lin'

from abc import ABCMeta, abstractmethod

import model.CandidateAnswer
import model.Question


class CandidateAnswerFilter(metaclass=ABCMeta):
    @abstractmethod
    def filter(self, question, candiateanswer):
        pass
