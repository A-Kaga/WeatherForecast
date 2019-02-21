# WeatherForecast
![image](https://github.com/A-Kaga/WeatherForecast/blob/master/images/colourful_cloud.png)  
感谢彩云天气提供的服务（此处应有logo）
### 进展
2018/12/3 项目开始  
2018/12/4 重构原有代码，框架大体完成  
2018/12/6 主体功能已实现，示意图见下：  
![image](https://github.com/A-Kaga/WeatherForecast/blob/master/images/test_pc.png)  

![image](https://github.com/A-Kaga/WeatherForecast/blob/master/images/test_phone.PNG) 
### 简介
一个简单的，~~脱裤放屁的~~python的练手项目。
做这个项目的初衷，是嫌彩云天气的每日天气推送推送时间不合适，推送内容也太繁杂，并且想要一个下雨提前通知的功能。于是花了点时间，写了个小项目。
通过调用彩云天气的API(https://dashboard.caiyunapp.com/user/sign_in/), 结合IFFTTT，实现以下功能：

    每日天气信息通知
    带伞通知（下雨前一个小时推送消息）
    极端天气预警

实际上是第一次尝试用oop思想开发，能体会到其博大精深，Forecast_oop是用oop思想重构的代码。  
~~该项目仍在更新中。  ~~
基本功能实现了，不打算继续完善了。

### 彩云天气API介绍
彩云天气提供了非常实用的天气数据API，提供诸如实时天气数据和分钟级、小时级、日级天气预报，天气预警等信息。  
开发者可以通过注册账号，提交申请，免费调用API接口，限制为每日1000次，超过该限制请咨询商业使用付费标准。  
API官方文档：http://wiki.caiyunapp.com/index.php/%E5%BD%A9%E4%BA%91%E5%A4%A9%E6%B0%94API/v2  

### IFTTT介绍
IFTTT是“if this then that”的缩写，IFTTT旨在帮助人们利用各网站的开放API，将Facebook、Twitter等各个网站或应用衔接，完成任务。
通过其提供的Webhooks服务，向该后台发送消息，就能给安装其对应app的手机发送通知，以实现各项天气服务。
IFTTT还有很多玩法，如果不会写ios应用，它应该会帮你很大的忙。
详情请百度。

### 问题和反思
我就提一个问题，太咕了，快三个月了才把文档写完.... 
