# livep
some tools to process live 直播处理的部分文件  
  
xmlp.py处理B站录播姬的xml弹幕文件，把所有类型的弹幕一律转化成滚动弹幕，SC（醒目留言）转化成固定弹幕，可以后续输入danmufactory生成ass文件  
xmlp_v2.py更新了SC的格式  
  
main.py是real-url弹幕部分main文件的改写，把print改为输入文件，这样可以后续生成ass文件压到视频里  
  
SCp.py把SC弹幕位置上移，软件处理出来自动放在屏幕中间了，现在处理后自动置顶
  
处理流程是danmu.xml----xmlp_v2.py---->new.ass----SCp.py---->new_SC.ass
