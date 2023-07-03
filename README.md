# livep
some tools to process live 直播处理的部分文件  
  
xmlp.py处理B站录播姬的xml弹幕文件，把所有类型的弹幕一律转化成滚动弹幕，SC（醒目留言）转化成固定弹幕，可以后续输入danmufactory生成ass文件  
xmlp_v2.py更新了SC的格式    
xmlp_v3.py增加了输出最多种类弹幕的功能，便于去除抽奖弹幕  
  
main.py是real-url弹幕部分main文件的改写，把print改为输入文件，这样可以后续生成ass文件压到视频里  
  
SCp.py把SC弹幕位置上移，软件处理出来自动放在屏幕中间了，现在处理后自动置顶  
  
处理流程是danmu.xml----xmlp_v2.py---->new.ass----SCp.py---->new_SC.ass  

flv2m4a.py是调用ffmpeg把某个目录中所有的flv文件中的音频抽取出来（m4a格式），存在原目录下，并**删除**原flv文件  

config.json是为了方便linux下载的录播姬配置文件  

command.sh 调用onedrive开始上传  
sensor.sh 检测网速不大时调用command.sh  
timer.sh 每天凌晨调用sensor.sh  
