'''
学生成绩管理器----创建一个Student类，记录他们的名字
，平均分和各门考试分数和他们的成绩等级。
'''
import numpy as np
import pandas as pd


class StudentError(Exception):
    pass


class Student():
    '''
    1,可以统计某一门课的平均分
       def subject_avg
    2,可以统计某一期考试的总分(各科的总分)
       def term_sum
    3,可以得到某门课的等级，>=90 A,80到89 B,70到79 C, 60到69 D, 剩下E
       def get_subject_grade
    4,打印某一期所有课的分数
    5,能显示这个实例的name和所有分数等级,打印成表格形式
       def print_grade_tables
      类似
       tom     math  english  sport     
        1       A       D       B       
        2       B       C       C       
        3       B       C       B
         。。。。。
    '''
    _subject = ('math', 'english', 'sport')
    def __init__(self, name):
        self._name = name
        '''
        _scores是一个pandas的DataFrame，columns是_subject
        index是每一期的编号
                math  english  sport     
        1       A       D       B       
        2       B       C       C       
        3       B       C       B
        '''
        self._scores = pd.DataFrame(np.zeros((10, 3)), index=range(1,11), columns=self._subject)

    def __repr__(self):
        return str(self._scores)

    def add_score(self, subject, term, score):
        if subject not in self._subject:
            raise StudentError('not a subject')
        if not isinstance(score, (int, float)):
            raise StudentError('invalid score')
        if not 0 <= score <= 100:
            raise StudentError('invalid score')
        self._scores.ix[term, subject] = score

    def subject_avg(self, subject):
        '''
        某门课的平均分
        '''
        pass

    def term_sum(self, term):
        pass

    def get_subject_grade(self, subject, term):
        pass

    def get_term_grades(self, term):
        pass

    def print_grade_tables(self):
        pass
        


def _test():
    s = Student('tom')
    s.add_score('math', 1, 95)
    s.add_score('math', 2, 81)
    s.add_score('math', 3, 86)
    s.add_score('english', 1, 66)
    #s.add_score('english', 2, 79)
    s.add_score('english', 3, 74)
    s.add_score('sport', 1, 85)
    s.add_score('sport', 2, 74)
    s.add_score('sport', 3, 83)
    #print(s)
    
    #s.subject_avg('sport')
    #s.term_sum(1)
    #s.get_subject_grade('english', 1)
    #s.get_term_grades(2)
    #s.print_grade_tables()

if __name__ == '__main__':
    _test()