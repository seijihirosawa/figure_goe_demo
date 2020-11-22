from django import forms # Djangoが準備しているforms
from .models import Jump # models.pyの部分で定義したDBのテーブル
from django.contrib.auth.forms import AuthenticationForm

#インプットフォーム
class InputForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InputForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
    # 定義以外の設定を行うクラス
    class Meta:
        model = Jump
        # models.pyのカラムの中で表示しないものをリストに保存
        exclude = ['id', 'score', 'registered_date','comment']

#ログインフォーム
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label