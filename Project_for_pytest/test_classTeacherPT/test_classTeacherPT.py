def test_init_teacher(teacher_test):
    assert teacher_test.__init__('test_name', 'test_education', 'test_experience', 'test_phone') == None
    assert len(teacher_test.teacher_dict) == 1
    assert teacher_test.teacher_dict['test_phone'] == 'test_name'


def test_get_name(teacher_test):
    assert teacher_test.get_name() == 'test_name'


def test_get_education(teacher_test):
    assert teacher_test.get_education() == 'test_education'


def test_get_experience(teacher_test):
    assert teacher_test.get_experience() == 'test_experience'


def test_set_experience(teacher_test):
    teacher_test.set_experience('test_new_experience')
    assert teacher_test.get_experience() == 'test_new_experience'
    teacher_test.set_experience('test_experience')


def test_get_phone(teacher_test):
    assert teacher_test.get_phone() == 'test_phone'


def test_get_teacher_data(teacher_test):
    assert teacher_test.get_teacher_data() == 'test_name, образование test_education, опыт работы test_experience год(-а)(лет).'


def test_add_mark(teacher_test):
    assert teacher_test.add_mark('name_student_test',
                                 'mark_test') == 'test_name поставила оценку mark_test ученику name_student_test'


def test_remove_mark(teacher_test):
    assert teacher_test.remove_mark('name_student_test',
                                    'mark_test') == 'test_name удалила оценку mark_test ученику name_student_test'


def test_give_a_consultation(teacher_test):
    assert teacher_test.give_a_consultation('grade_test') == 'test_name провёла консультацию в классе grade_test'


def test_fire_teacher(teacher_test):
    assert teacher_test.fire_teacher() == 'Преподаватель test_name был уволен'
    assert teacher_test.fire_teacher() == 'Преподавателя test_name уже уволили'
    assert teacher_test.teacher_dict == {}


def test_init_discipline_teacher(discipline_teacher_test):
    assert discipline_teacher_test.__init__('test_name', 'test_education', 'test_experience', 'test_discipline',
                                            'test_job_title', 'test_phone') == None


def test_get_job_title(discipline_teacher_test):
    assert discipline_teacher_test.get_job_title() == 'test_job_title'


def test_set_job_title(discipline_teacher_test):
    discipline_teacher_test.set_job_title('test_new_job_title')
    assert discipline_teacher_test.get_job_title() == 'test_new_job_title'
    discipline_teacher_test.set_job_title('test_job_title')


def test_get_discipline_teacher_data(discipline_teacher_test):
    assert discipline_teacher_test.get_teacher_data() == 'test_name, образование test_education, опыт работы test_experience год(-а)(лет).\nПредмет test_discipline, должность test_job_title'


def test_discipline_teacher_add_mark(discipline_teacher_test):
    assert discipline_teacher_test.add_mark('name_student_test', 'mark_test') == 'test_name поставила оценку mark_test ученику name_student_test\nПредмет: test_discipline'


def test_discipline_teacher_remove_mark(discipline_teacher_test):
    assert discipline_teacher_test.remove_mark('name_student_test', 'mark_test') == 'test_name удалила оценку mark_test ученику name_student_test\nПредмет: test_discipline'


def test_discipline_teacher_give_a_consultation(discipline_teacher_test):
    assert discipline_teacher_test.give_a_consultation('grade_test') == 'test_name провёла консультацию в классе grade_test\nПо предмету test_discipline как test_job_title'