'''
学生成绩管理器----记录一个班级的学生（创建一个Student类，记录他们的名字
，平均分和各门考试分数）和他们的成绩等级。根据学生的测验和作业的分数计算
出平均分和成绩等级
'''


class StudentError(Exception):
    pass


class Student():
    # 可以统计某个人某一科的总分
    # 可以统计某个人某一期考试的总分
    # 可以统计几个学生某一个科目每一期的总分
    _subject = ('math', 'english', 'sport')
    # 做一个装饰器，检查subject是否在_subject中
    def __init__(self, name):
        self._name = name
        # scores的键是学科_期数，比如math_1
        self._scores = dict()

    def add_score(self, subject, time, score):
        if subject not in self._subject:
            raise StudentError('not a subject')
        key = ''.join([str(subject), '_', str(time)])
        self._scores.update({key: score})

    def subject_sum(self, subject):
        if subject not in self._subject:
            raise StudentError('not a subject')
        _subject_sum = 0
        for key, score in self._scores.items():
            if key.startswith(subject):
                _subject_sum += score
        print(_subject_sum)
        return _subject_sum


    def __str__(self):
        return str(self._scores)

s = Student('tom')
s.add_score('math', 1, 99)
s.add_score('math', 2, 80)
print(s)

s.subject_sum('math')
