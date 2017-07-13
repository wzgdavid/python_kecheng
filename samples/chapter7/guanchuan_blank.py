'''
学生成绩管理器----创建一个Student类，记录他们的名字
，平均分和各门考试分数和他们的成绩等级。
'''


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
    4,打印某一期所有课的分数,做成一个字典
       def get_term_grades
      比如第一期的所有等级如下
        {'math': 95, 'english': 66, 'sport': 85}
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
        _scores的键是学科_期数，比如math_1
        _scores 是类似这样的一个字典
        {
            'math_1': 99, 
            'math_2': 80,
            'english_1':90,
            'english_2':77
        }
        '''
        self._scores = dict()

    def add_score(self, subject, term, score):
        if subject not in self._subject:
            raise StudentError('not a subject')
        if not isinstance(score, (int, float)):
            raise StudentError('invalid score')
        if not 0 <= score <= 100:
            raise StudentError('invalid score')
        key = ''.join([str(subject), '_', str(term)])
        self._scores.update({key: score})


    def term_sum(self, term):
        pass

    def subject_avg(self, subject):
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
    
    #s.subject_avg('english')
    #s.term_sum(2)
    #s.get_subject_grade('math', 1)
    #s.get_term_grades(2)
    #s._get_termgscores(2)
    #s.print_grade_tables()

if __name__ == '__main__':
    _test()