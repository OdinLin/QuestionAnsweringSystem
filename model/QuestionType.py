#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'odin-lin'


class QuestionType(object):

    NULL = 0
    PERSON_NAME = 1
    LOCATION_NAME = 2
    ORGANIZATION_NAME = 3
    NUMBER = 4
    TIME = 5
    DEFINITIION = 6
    OBJECT = 7

    @staticmethod
    def get_nature(index):
        # nr 人名
        # nr1 汉语姓氏
        # nr2 汉语名字
        # nrj 日语人名
        # nrf 音译人名
        # ns 地名
        # nsf 音译地名
        # nt 机构团体名
        # m 数词
        # mq 数量词
        # t 时间词
        # tg 时间词性语素
        natures = ['unknow', 'nr', 'ns', 'nt', 'm', 't']

        return natures[index]