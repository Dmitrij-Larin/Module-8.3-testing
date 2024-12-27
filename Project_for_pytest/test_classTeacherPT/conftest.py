import pytest

from Project_for_pytest.classDisciplineTeacher import DisciplineTeacher
from Project_for_pytest.classTeacher import Teacher


@pytest.fixture
def teacher_test():
    Teacher.teacher_dict.clear()
    teacher = Teacher('test_name', 'test_education', 'test_experience', 'test_phone')
    return teacher


@pytest.fixture
def discipline_teacher_test():
    DisciplineTeacher.teacher_dict.clear()
    discipline_teacher = DisciplineTeacher('test_name', 'test_education', 'test_experience', 'test_discipline',
                                           'test_job_title', 'test_phone')
    return discipline_teacher
