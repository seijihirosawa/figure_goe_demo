from django.shortcuts import render,redirect
from .forms import InputForm, LoginForm

import joblib
import numpy as np
from .models import Jump

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

#モデルの読み込み
loaded_model = joblib.load("model/lightgbm_for_KIKAGAKU.pkl")

@login_required
def result(request):
    #最新のジャンプデータの取得
    data = Jump.objects.order_by("id").reverse().values_list("group_number","event","unique_entry","height","distance","landing_speed")

    #推論の実行と表示
    x = np.array([data[0]])
    y = loaded_model.predict(x)#予測点の算出
    score = y[0]

#コメントの表示
    # 追加:結果に基づいてコメントを返す
    if 0 <= score <= 1:
        comment = 'まずまずの得点です'
    elif 1 < score <= 2:
        comment = '良い得点のジャンプです'
    elif 2 < score <= 3:
        comment = '素晴らしい得点です'
    elif 3 < score <= 4:
        comment = '世界選手権表彰台クラスの得点です'
    elif 4 < score <= 5:
        comment = "オリンピックチャンピオンもびっくりの得点です"

    #推論結果を保存
    jump = Jump.objects.order_by("id").reverse()[0]
    jump.score = score
    jump.comment = comment
    jump.save()


    #推論結果をHTMLに渡す
    return render(request, 'result.html', {'score':score,'comment':comment})


# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def input_form(request): # 入力フォームに値を入れたときの処理
    if request.method == "POST":
        form = InputForm(request .POST)#入力データの取得
        if form.is_valid():
            form.save()#入力を保存
            return redirect("result") #indexのページを表示
    else:
        form = InputForm()
        return render(request, 'input_form.html', {'form':form})
@login_required
def history(request):
    print("here")
    if request.method == 'POST':
        print("here") # POSTメソッドが送信された場合
        d_id = request.POST # POSTされた値を取得→顧客ID
        d_jump = Jump.objects.filter(id=d_id['d_id']) # filterメソッドでidが一致するCustomerを取得
        d_jump.delete() # 顧客データを消去
        jumps = Jump.objects.all() # 顧客全データを取得
        return render(request, 'history.html', {'jumps':jumps})
    else:
        jumps = Jump.objects.all()
        return render(request, 'history.html', {'jumps':jumps})

# ログインページ
class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

# ログアウトページ
class Logout(LogoutView):
    template_name = 'base.html'