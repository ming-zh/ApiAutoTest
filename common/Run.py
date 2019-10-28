# -*- coding: utf-8 -*-#
2
3  # ------------------------------------
4  # Name:         Run
5  # Description:  
6  # Author:       17621158197
7  # Date:         2019/10/17
8  # ------------------------------------

import unittest
from ddt import ddt, data, unpack
from common.readXlsx import ReadXlsx
from common import request, writeXlsx
import ast, json
import datetime as dt


@ddt
class Run(unittest.TestCase):
    d = ReadXlsx().read('Sheet1')

    @data(*d)
    @unpack
    def test_run(self, value1, value2, value3, value4, value5, value6, value7, value8, value9):
        """  headers 和 parameters 必须使用 ast.literal_eval(value)函数转化为dict才能使用，为空的时候转化会报错，所以要做判断
        :param value1: title
        :param value2: host
        :param value3: path
        :param value4: method
        :param value5: headers
        :param value6: parameters
        :param value7: expect
        """
        '''
        将参数转化为字典时，需要加判断，如果不为空在转化，否则会抛出异常
        '''
        if value5 and value6:
            value5 = ast.literal_eval(value5)
            value6 = ast.literal_eval(value6)
        elif value5:
            value5 = ast.literal_eval(value5)
        elif value6:
            value6 = ast.literal_eval(value6)
        else:
            pass

        '''
        判断请求方法
        '''
        if value4 == 'post':
            r = request.post(value2 + value3, value5, value6)
            if self.assertEqual(int(value7), eval(value8)):
                result = 'fail'
            else:
                result = 'pass'
            writeXlsx.writeContent('../reports/report', int(value9)+4, value1, r.text, value7, result)
        elif value4 == 'get':
            r = request.get(value2 + value3, value5, value6)
            if self.assertEqual(int(value7), eval(value8)):
                result = 'fail'
            else:
                result = 'pass'
            writeXlsx.writeContent('../reports/report', int(value9)+4, value1, r.text, value7, result)
        else:
            pass


if __name__ == '__main__':
    ''' writeXlsx.writeBook()方法须在此处调用，才能首次创建文件
    '''
    currentTime = dt.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
    writeXlsx.writeBook('../reports/report', '机器人接口自动化测试报告', currentTime)
    unittest.main(verbosity=1)

