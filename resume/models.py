from django.db import models

# Create your models here.
class Resume(models.Model) :
    gender = models.CharField(max_length = 100)  #家长性别
    tel = models.CharField(max_length = 50, blank = True)  #家长电话
    date_time = models.DateTimeField(auto_now_add = True)  #填写日期
    address = models.TextField(blank = True, null = True)  #家教地址
    grade = models.CharField(max_length = 50, blank = True)   #孩子年级
    上门时间 = models.TextField(blank = True, null = True) #上门时间
    家教要求 = models.TextField(blank = True, null = True)   #家教要求
    孩子基本信息 = models.TextField(blank = True, null = True)  #基本信息
        

    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.tel

    class Meta:  #按时间下降排序
        ordering = ['-date_time']
