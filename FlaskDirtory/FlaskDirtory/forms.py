import wtforms  #定义字段
from flask_wtf import FlaskForm #定义表单的父类
from wtforms import validators  #定义校验

from FlaskDirtory.models import Course

class TeacherForm(FlaskForm):
    """
    form字段的参数
    label=None, 表单的标签
    validators=None, 校验，传入校验的方法
    filters=tuple(), 过滤
    description='',  描述
    id=None, html id
    default=None, 默认值
    widget=None,
    render_kw=None,
    """
    course = Course.query.all()
    cou_list = [(cou.id, cou.course_name) for cou in course]
    name = wtforms.StringField("教师姓名",
                               render_kw = {
                                   "class": "form-control",
                                   "placeholder": "教师姓名",

                               },
                               validators = [
                                   validators.DataRequired("姓名不可以为空")
                               ]
    )
    age = wtforms.IntegerField("教师年龄",
                               render_kw={
                                   "class": "form-control",
                                   "placeholder": "教师年龄"
                               },
                               validators=[
                                   validators.DataRequired("年龄不可以为空")
                               ]
    )
    gender = wtforms.StringField("教师性别",
                                render_kw = {
                                    "class": "form-control",
                                    "placeholder": "教师年龄"
                                },
                                validators=[
                                     validators.DataRequired("性别不可以为空")
                                ]
    )

    course = wtforms.SelectField(
        "学科",
        choices=cou_list,
        render_kw={
            "class": "form-control",
        }
    )
