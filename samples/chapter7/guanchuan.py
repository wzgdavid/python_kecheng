'''
学生成绩管理器----记录一个班级的学生（创建一个Student类，记录他们的名字
，平均分和各门考试分数）和他们的成绩等级。
'''
'''
现在是用字典做，学了pandas后此题用pandas做
'''

class StudentError(Exception):
    pass


class Student():
    '''

    1,可以统计某一门课的平均分
    2,可以统计某一期考试的总分(各科的总分)
    3,可以得到某门课的等级，>=90 A,80到89 B,70到79 C, 60到69 D, 剩下E
    4,打印某一期所有课的等级,做成一个字典，
      比如第一期的所有等级如下

    5,print一个Student实例，能显示这个实例的name和所有分数等级,打印成表格形式
      比如
          s = Student('tom')
          print(s)
      会显示类似如下内容
         grades of tom is
             math  english  sport
         1     A       A       B
         2     C       D       C 
         3     A       B       B
         。。。。。
    '''
    _subject = ('math', 'english', 'sport')
    # 做一个装饰器，检查subject是否在_subject中
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

    # --------------------------------这个类中以下的部分让学生做-----------------------------

    def term_sum(self, term):
        '''一期总分'''
        #if term not in self._subject:
        #    raise StudentError('not a subject')
        term_sum = 0
        for key, score in self._scores.items():
            if key.endswith(str(term)):
                term_sum += score
        print(term_sum)
        return term_sum

    def subject_avg(self, subject):
        '''
        某门课的平均分
        '''
        if subject not in self._subject:
            raise StudentError('not a subject')
        subject_sum = 0
        cnt = 0
        for key, score in self._scores.items():
            if key.startswith(subject):
                subject_sum += score
                cnt += 1
        avg = subject_sum/cnt
        print(avg)
        return avg

    def _get_subject_name(self, subject, term):
        return ''.join((subject, '_', str(term)))

    def get_grade(self, subject, term):
        '''得到某门课的等级'''
        if subject not in self._subject:
            raise StudentError('not a subject')
        # 常用可以写成一个私有函数，方便调用
        # subject_name = ''.join((subject, '_', str(term)))
        subject_name = self._get_subject_name(subject, term)
        score = self._scores.get(subject_name, 0)
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'E'
        print(grade)
        return grade

    def get_termgrades(self, term):
        '''某一期所有课的等级,做成一个字典'''
        grades = {}
        for subject in self._subject:
            subject_name = self._get_subject_name(subject, term)
            grades[subject] = self._scores.get(subject_name)
        print(grades)

    def __str__(self):
        return str(self._scores)

def _test():
    s = Student('tom')
    s.add_score('math', 1, 95)
    s.add_score('math', 2, 81)
    s.add_score('math', 3, 86)
    s.add_score('english', 1, 66)
    s.add_score('english', 2, 79)
    s.add_score('english', 3, 74)
    s.add_score('sport', 1, 85)
    s.add_score('sport', 2, 74)
    s.add_score('sport', 2, 83)
    #print(s)
    
    s.subject_avg('english')
    s.term_sum(2)
    s.get_grade('math', 1)
    s.get_termgrades(1)

if __name__ == '__main__':
    _test()