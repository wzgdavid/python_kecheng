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
       def subject_avg
    2,可以统计某一期考试的总分(各科的总分)
       def term_sum
    3,可以得到某门课的等级，>=90 A,80到89 B,70到79 C, 60到69 D, 剩下E
       def get_subject_grade
    4,打印某一期所有课的分数,做成一个字典，
       def get_term_grades
      比如第一期的所有等级如下
        {'math': 95, 'english': 66, 'sport': 85}
    5,能显示这个实例的name和所有分数等级,打印成表格形式
       def print_grade_tables
      比如
         tom   math  english  sport
          1     99      88       99
          2     99      88       77
          3     66      44       65
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

    def get_subject_grade(self, subject, term):
        '''得到某门课的等级'''
        if subject not in self._subject:
            raise StudentError('not a subject')
        # 常用可以写成一个私有函数，方便调用
        # subject_name = ''.join((subject, '_', str(term)))
        subject_name = self._get_subject_name(subject, term)
        score = self._scores.get(subject_name, 0)
        grade = self._get_score_grade(score)
        return grade

    def _get_score_grade(self, score):
        '''提取出来作为一个私有方法，'''
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
        return grade

    def get_term_grades(self, term):
        '''某一期所有课的等级,做成一个字典'''
        grades = {}
        for subject in self._subject:
            subject_name = self._get_subject_name(subject, term)
            grades[subject] = self._scores.get(subject_name)
        print(grades)
        return grades

    def _get_termgscores_list(self, term):
        '''某一期所有课的分数,做成一个list, 为print成绩等级表格做准备'''
        grades = []
        for subject in self._subject:
            subject_name = self._get_subject_name(subject, term)
            score = self._scores.get(subject_name)
            grades.append(score)
        #print(grades)
        return grades

    def print_grade_tables(self):
        '''把整个表看成一个每行最后一个元素是'\n'的列表'''
        grades_tables = ['tom']
        grades_tables.extend(self._subject)
        grades_tables.append('\n')
        for n in range(1,9): # 按期数循环
            row = [str(n)] # 每一行的标号
            termgrades_list = self._get_termgscores_list(n)
            if not any(termgrades_list): # 如果某一期全部为None，则认为没有这一期成绩
                continue
            #termgrades_list = [str(n) for n in termgrades_list]  # 分数
            termgrades_list = [self._get_score_grade(n) for n in termgrades_list] # 如果要全打印等级
            row.extend(termgrades_list)  # 每一行的等级
            row.append('\n')             # 每一行最后一个元素，换行符
            #print(row)
            grades_tables.extend(row)

        #print(grades_tables)
        for n in grades_tables:
            print(n.center(8), end='')


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
    s.add_score('sport', 3, 83)
    #print(s)
    
    s.subject_avg('english')
    s.term_sum(2)
    s.get_subject_grade('math', 1)
    s.get_term_grades(1)
    s._get_termgscores_list(1)
    s.print_grade_tables()

if __name__ == '__main__':
    _test()