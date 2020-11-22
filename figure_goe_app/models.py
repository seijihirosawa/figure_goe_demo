from django.db import models
from datetime import date

class Jump(models.Model):
    event_options = (
        (0, "short_program"),
        (1, "free_skating")
    )

    unique_entry_options = (
        (0, "No"),
        (1, "Yes")
    )

    #カラム相当変数
    id = models.AutoField(primary_key = True)
    group_number = models.IntegerField("滑走グループ", default=1)
    event = models.IntegerField("イベント", choices = event_options, default=0)
    unique_entry = models.IntegerField("ジャンプの前の工夫", choices = unique_entry_options,default=0)
    height = models.FloatField("高さ(m)", default=0.00)
    distance = models.FloatField("幅(m)", default=0.00)
    landing_speed = models.FloatField("着氷スピード(km/h)",default=0.00)
    score = models.FloatField(default=0.00)
    comment = models.CharField(max_length=200, blank=True, null=True)
    registered_date = models.DateField(default=date.today()) #default=date.today() : 本日の日付をデフォルトに設定
    
    #管理画面の表示
    def __str__(self):
        if self.score == 0.0:
            return "%s, %s" % (self.registered_date.strftime("%Y-%m-%d"),self.id)
        else:
            return "%s, %s ,%s" % (self.registered_date.strftime("%Y-%m-%d"),self.id,"{}点".format(self.score))