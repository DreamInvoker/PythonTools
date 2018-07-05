# Python 工具

## 一、发短信
>  使用Twilio官网提供的免费的信息服务，每个月15美元的额度
>  使用前请安装twilio：pip install twilio
>  每条短信0.028美元，每个月可以发500多条短信，所以尽量只在需要的时候调用该接口发送短信。
    
### 1. 安装依赖
```commandline
pip install twilio
```

### 2.拷贝功能
> 将sendSMS.py拷贝到需要发短信的项目中

### 3. 使用
```python
import sendSMS as sms

# 可以修改函数，设置默认的短信接收人to
# 电话号码前要加上+86
sms.send(msg='hello wyt!',to="+86***********") 
```

## 二、打印进度

### 1. 使用例子

```python
from printProcess import show
import time
import datetime

total = 333 #总数
c = 0 #计数
start = datetime.datetime.now()
while c <= total:
    show(c,total,interval=datetime.datetime.now()-start,DoneInfo='Finished')
    c += 1
    time.sleep(0.1)
```