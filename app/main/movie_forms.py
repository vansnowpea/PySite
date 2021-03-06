# encoding: utf-8
from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SelectField, SubmitField, FileField, ValidationError
from wtforms.validators import DataRequired, Length, URL, Regexp

from ..models.movie import Poster, str_movie_type


class AddPosterForm(Form):
    name = StringField(u'电影名', validators=[DataRequired(), Length(0, 50)])
    private = SelectField(u'是否公开', choices=[(0, u'所有人可见'), (1, u'仅自己可见')], coerce=int)
    douban_link = StringField(u'豆瓣链接', validators=[Length(0, 80), URL()])
    method = SelectField(u'上传方式', choices=[(u'file', u'本地图片'), (u'url', u'网络图片')], validators=[Regexp(u'^file|url$')])
    img_file = FileField(u'海报图片')
    img_url = StringField(u'海报URL', validators=[])
    o_name = StringField(u'原名', validators=[Length(0, 50)])
    alias = StringField(u'别名', validators=[Length(0, 160)])
    director = StringField(u'导演', validators=[Length(0, 40)])
    screenwriter = StringField(u'编剧', validators=[Length(0, 40)])
    performers = StringField(u'主演', validators=[Length(0, 200)])
    type = SelectField(u'类型', coerce=int)
    country = StringField(u'地区', validators=[Length(0, 100)])
    length = StringField(u'片长', validators=[Length(0, 60)])
    release_date = StringField(u'上映日期', validators=[Length(0, 60)])
    introduction = TextAreaField(u'电影简介')
    submit = SubmitField(u'提交')

    def __init__(self, *args, **kwargs):
        super(AddPosterForm, self).__init__(*args, **kwargs)
        types_list = str_movie_type.split(u',')
        self.type.choices = [(i+1, types_list[i]) for i in range(0, len(types_list))]

    def validate_name(self, field):
        if Poster.query.filter_by(name=field.data).first():
            raise ValidationError(u'该电影已经存在，不能重复添加。')


class EditPosterForm(Form):
    name = StringField(u'电影名', validators=[DataRequired(), Length(0, 50)])
    private = SelectField(u'是否公开', choices=[(0, u'所有人可见'), (1, u'仅自己可见')], coerce=int)
    douban_link = StringField(u'豆瓣链接', validators=[Length(0, 80), URL()])
    method = SelectField(u'上传方式', choices=[(u'file', u'本地图片'), (u'url', u'网络图片')], validators=[Regexp(u'^file|url$')])
    img_file = FileField(u'海报图片')
    img_url = StringField(u'海报URL', validators=[])
    o_name = StringField(u'原名', validators=[Length(0, 50)])
    alias = StringField(u'别名', validators=[Length(0, 160)])
    director = StringField(u'导演', validators=[Length(0, 40)])
    screenwriter = StringField(u'编剧', validators=[Length(0, 40)])
    performers = StringField(u'主演', validators=[Length(0, 200)])
    type = SelectField(u'类型', coerce=int)
    country = StringField(u'地区', validators=[Length(0, 100)])
    length = StringField(u'片长', validators=[Length(0, 60)])
    release_date = StringField(u'上映日期', validators=[Length(0, 60)])
    introduction = TextAreaField(u'电影简介')
    submit = SubmitField(u'提交')

    def __init__(self, *args, **kwargs):
        super(EditPosterForm, self).__init__(*args, **kwargs)
        types_list = str_movie_type.split(u',')
        self.type.choices = [(i+1, types_list[i]) for i in range(0, len(types_list))]


class AddStillForm(Form):
    time_min = StringField(u'时间（分）', validators=[Regexp(u'^\d{0,3}$', message=u'最大支持999分钟')])
    time_sec = StringField(u'时间（秒）', validators=[Regexp(u'^[0-5]?\d?$', message=u'不在0-59秒范围内')])
    private = SelectField(u'是否公开', choices=[(0, u'所有人可见'), (1, u'仅自己可见')], coerce=int)
    method = SelectField(u'上传方式', choices=[(u'file', u'本地图片'), (u'url', u'网络图片')], validators=[Regexp(u'^file|url$')])
    img_file = FileField(u'剧照图片')
    img_url = StringField(u'剧照URL', validators=[])
    comment = StringField(u'我想说')
    submit = SubmitField(u'提交')


class EditStillForm(Form):
    time_min = StringField(u'时间（分）', validators=[Regexp(u'^\d{0,3}$', message=u'最大支持999分钟')])
    time_sec = StringField(u'时间（秒）', validators=[Regexp(u'^[0-5]?\d?$', message=u'不在0-59秒范围内')])
    private = SelectField(u'是否公开', choices=[(0, u'所有人可见'), (1, u'仅自己可见')], coerce=int)
    comment = StringField(u'我想说')
    submit = SubmitField(u'更新')
