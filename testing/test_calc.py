#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from python_code.calc import Calc
import yaml


def setup_module():
    print("setup module")


def teardown_module():
    print("teardown module")


class TestCalc:

    def setup_class(self):
        print("setup_class")
        self.calc = Calc()

    def teardown_class(self):
        print("teardown_class")

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    @pytest.mark.parametrize('a, b, expect', )
    def test_add_1(self, a, b, expect):
        for i in range(5):
            result = self.calc.add(a, b)
            print(f"result = {result}")
            assert result == expect

    # def test_add_2(self):
    #     datalist = [
    #         (1,1,2),
    #         (0.1, 0.2, 0.3),
    #         (100, 200, 300),
    #     ]
    #     result = self.calc.add(1, 1)
    #     print(f"result = {result}")
    #     assert result == 2
    #
    #     result = self.calc.add(0.1, 0.2)
    #     print(f"result = {result}")
    #     assert result == 0.3
    #
    #     result = self.calc.add(100, 200)
    #     print(f"result = {result}")
    #     assert result == 300

    #
    # def test_add_3(self):
    #     result = self.calc.add(100, 200)
    #     print(f"result = {result}")
    #     assert result == 300
    #
    # def test_add_4(self):
    #     result = self.calc.add(0, 1)
    #     print(f"result = {result}")
    #     assert result == 1

    def test_div_1(self):
        result = self.calc.div(1, 1)
        print(f"result = {result}")
        assert result == 1


if __name__ == '__main__':
    pytest.main(['test_calc.py'])
