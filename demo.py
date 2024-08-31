VISION = '0.1.3'
print(f'loading... v{VISION}')

import time
import arts
import codecs
import toolbox
import threading  
import art_player
from sys import exit as quit
from colorama import Fore, Back
from prompt_toolkit import prompt
from htmlword import setting as setbox
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
# from toolbox import better_print as print
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion.word_completer import WordCompleter
print('载入支持库成功')

email=[]
anegg=0
stop_event=''

try:#导入设置
    with codecs.open('email.PRCS', 'r', 'utf-8') as f:
        lintnum=0
        while True:
            
            line = f.readline().replace('\n', '').replace('\r', '')

            if not line:
                break

            email.append(line)

            lintnum+=1

except:
	input('Error: Unable to find email.PRCS! Automatically generated.')
	time.sleep(3)
	exit()
print('导入邮件成功')

address = ''
port = 25565
titleinformation=''
times=10
maxline=0
mode=True
xianczhuangt=False
mader = ''
CHVISION = ''
CKT=False

session = PromptSession()

com=['exit','set_ip','help','start','set_port','set_connect_time','stop','show','test_connect','check_update','clear','vision']
com_mean = ['退出程序','设置查找IP','获取帮助','启动查找线程','设置连接端口','设置查找间隔','停止查找线程','显示设置信息','连接测试','查找更新','清空屏幕','显示Potato-土豆风控版本']


Completer = WordCompleter(com,
                             ignore_case=True)

style = Style.from_dict({
    # User input (default text).
    '':          '#FFA500',

    # Prompt.
    'pound':    '#FFFFFF',
    'path':     '#FFFFFF',
})


message = [
    ('class:path',     'Potato-土豆风控:'),
    ('class:pound',    '# '),
]
question = [
    ('class:path',     ''),
    ('class:pound',    '# '),
]
print('变量部署成功')

def listen_setver(IP,port,times):#查找子函数
	global mode,VISION,stop_event 
	while not stop_event.is_set():  
		status,protocol,version,title,numplayers,maxplayers,mode=toolbox.search_minecraft_server(IP,port)
		if status!='离线' and status!='未知状态':
			mode=True
		elif mode:
			realtime=toolbox.timebox.outputtimebox()
			mode=False
			print('检测到服务器出现异常')
			toolbox.Easytosend(email,setbox(realtime,IP,port))
			print(toolbox.timebox.outputtimebox()+'服务器出现异常,邮件已发送')

			file=open(f'log.txt','a')#log部分
			file.write(f'服务器于{times}发生崩溃 原因{status}\n')
			file.close()

def init():
	global maxline,VISION,mader,Fore,Back,CHVISION,CKT
	r=0
	for i in com:
		maxline = max(len(i),maxline)
		r+=1
	
	art_player.main()
	messages = arts.messages
	try:
		CKT=True
		mader=messages[1]
		CHVISION=messages[2]
		time.sleep(3)
		toolbox.clear()
	except:
		toolbox.print_fancy('获取失败',color=Fore.RED,background=Back.LIGHTRED_EX)
		time.sleep(3)
		toolbox.clear()
	time.sleep(3)

	

def main():
	global address,port,titleinformation,times,xianczhuangt,maxline,VISION,CHVISION,anegg,mader,stop_event
	while True:

		if address!='':#标题显示服务器信息
			if port!='':
				titleinformation = ' 服务器:'+address+':'+str(port)
			else:
				titleinformation = ' 服务器:'+address
		else:
			titleinformation = ''

		user_input =session.prompt(message,
							style=style,
							auto_suggest=AutoSuggestFromHistory(),
							completer=Completer,
							bottom_toolbar=f"Potato-土豆风控 V{VISION}{titleinformation}"
							)
		
		if user_input in com or user_input=='windows':#指令库

			if user_input=='exit':#退出
				anegg=0
				toolbox.clear()
				print('have a nice day!')
				quit()
				

			elif user_input=='set_ip':#设置服务器IP地址
				anegg=0
				temp =session.prompt(question,
								style=style,
								bottom_toolbar=f"Potato-土豆风控 V{VISION} 执行输入 命令:set_ip"
								)
				
				if temp!='' :
					address=str(temp)
			
			elif user_input=='set_port':#设置服务器端口
				anegg=0
				temp =session.prompt(question,
								style=style,
								bottom_toolbar=f"Potato-土豆风控 V{VISION} 执行输入 命令:set_port"
								)
				
				if temp!='' :
					port=int(temp)
				
			elif user_input=='show':#显示设置
				anegg=0
				if address!='':
					if port!='':
						print(address+':'+str(port))
					else:
						print(address)
				else:
					print('IP&port:NO information!')

				print(f'connect_time{times}')
				print(f'查找线程状态{xianczhuangt}')

			elif user_input=='test_connect':#连接测试
				anegg=0
				status,protocol,version,title,numplayers,maxplayers,mode=toolbox.search_minecraft_server(address,port)
				print("服务器状态:", status)
				if status!='离线' and status!='未知状态':
					print("协议版本:", protocol)
					print("游戏版本:",version)
					print("服务器标题:", title)
					print("当前玩家数:", numplayers)
					print("最大玩家数:", maxplayers)
			
			elif user_input=='set_connect_time':#设置服务器端口
				anegg=0
				temp =session.prompt(question,
								style=style,
								bottom_toolbar=f"Potato-土豆风控 V{VISION} 执行输入 命令:set_connect_time"
								)
				if temp!='' :
					times=int(temp)

			elif user_input=='start':#启动查找线程
				anegg=0
				if address != '':
					print('等待查找线程启动')
					stop_event = threading.Event()  
					# 创建并启动子线程  
					listen_thread = threading.Thread(target=listen_setver, args=(address,port,times))  
					listen_thread.start()
					print('查找线程已启动')
					xianczhuangt=True
				else:
					print('服务器地址错误')

			elif user_input=='stop':#停止查找线程
				anegg=0
				stop_event.set()  # 设置停止事件  
				print("等待查找线程结束")  
				listen_thread.join()  
				print("查找线程已结束")
				xianczhuangt=False
			
			elif user_input=='help':#帮助
				if anegg==True:
					print('No Help Available\n(so leave me alone)')
					anegg=0
				else:
					anegg=0
					r=0
					for i in com:
						spacenum=maxline+1-len(i)

						print(f'{i}{" "*spacenum}	{com_mean[r]}')
						r+=1

			elif user_input=='check_update':#新版本检测
				anegg=0
				if CHVISION != VISION:
					if CKT:
						print(f'检测到新版本 当前版本为{VISION}新版本为{CHVISION}')
					else:
						toolbox.print_fancy('获取失败',color=Fore.RED,background=Back.LIGHTRED_EX)
				else:
					print('程序已是最新版本')

			elif user_input=='clear':#清空屏幕
				toolbox.clear()
				anegg+=1
			
			elif user_input=='windows':#彩蛋
				if anegg==3:
					anegg=True
				else:
					anegg=0

			elif user_input == 'vision':#显示Potato-土豆风控版本
				anegg=0
				print(f'Potato-土豆风控 [版本 {VISION}]\n Made By {mader}')

		else:#命令不存在提示
			anegg=0
			if user_input!='':
				print('[腐竹的奇妙土豆猫]错误了呢喵~该命令不在我的数据库中呢喵~')
print('函数加载成功')


if __name__ == '__main__':
	init()
	main()