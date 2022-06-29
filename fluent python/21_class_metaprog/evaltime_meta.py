# -*- coding: utf-8 -*-
from evalsupport import deco_alpha
from evalsupport import MetaAleph

print('<[1]> evaltime_meta module start')

@deco_alpha
class ClassThree():
    print('<[2]> ClassThree body')

    def method_y(self):
        print('<[3]> ClassThree.method_y')

class ClassFour(ClassThree):
    print('<[4]> ClassFour body')

    def method_y(self):
        print('<[5]> ClassFour.method_y')

class ClassFive(metaclass=MetaAleph):
    print('<[6]> classFive body')

    def __init__(self):
        print('<7> classFive.__init__')

    def method_z(self):
        print('<[8]> ClassFive.method_z')

class ClassSix(ClassFive):
    print('<[9]> ClassSix body')

    def method_z(self):
        print('<[10]> ClassSix.method_z')

if __name__ == '__main__':
    print('<[11]> ClassThree tests', 30*'.')
    three = ClassThree()
    three.method_y()
    print('<[12]> ClassThree tests', 30*'.')
    four = ClassFour()
    four.method_y()
    print('<[13]> ClassThree tests', 30*'.')
    five = ClassFive()
    five.method_z()
    print('<[14]> ClassThree tests', 30*'.')
    six = ClassSix()
    six.method_z

print('<[15]> evaltime_meta module end')

"""
>>> import evaltime_meta
<[100]> evalsupport module start
<[400]> MetaAleph body
<[700]> evalsupport module end
<[1]> evaltime_meta module start
<[2]> ClassThree body
<[200]> deco_alpha
<[4]> ClassFour body
<[6]> classFive body
<[500]> MetaAleph.__init__
<[9]> ClassSix body
<[500]> MetaAleph.__init__
>>>
~/Project/liangpi/fluent python/21_class_metaprog  ‹master*› $ vim evaltime_meta.py
~/Project/liangpi/fluent python/21_class_metaprog  ‹master*› $ python3 evaltime_meta.py
<[100]> evalsupport module start
<[400]> MetaAleph body
<[700]> evalsupport module end
<[1]> evaltime_meta module start
<[2]> ClassThree body
<[200]> deco_alpha
<[4]> ClassFour body
<[6]> classFive body
<[500]> MetaAleph.__init__
<[9]> ClassSix body
<[500]> MetaAleph.__init__
<[11]> ClassThree tests ..............................
<[300]> deco_alpha:inner_1
<[12]> ClassThree tests ..............................
<[5]> ClassFour.method_y
<[13]> ClassThree tests ..............................
<7> classFive.__init__
<[600]> MetaAleph.__init__:inner_2
<[14]> ClassThree tests ..............................
<7> classFive.__init__
<[15]> evaltime_meta module end
"""
