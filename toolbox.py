import socket
import os
import time
from mail import SendMail
from time import localtime as loadtime
from colorama import Fore, Back, Style, init  

init(autoreset=True)

def search_minecraft_server(host,port=25565):
    try:
        status,protocol,version,title,numplayers,maxplayers,smode = "未知状态","\000","\000","\000","\000","\000",False
        #初始化变量
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.sendall(b'\xFE\x01')
        #向服务器发送请求
        data = s.recv(1024).split(b'\x00\x00')
        #把接受到的数据中00 00 之间的数据进行隔段操作以方便对数据操作
        s.close()
        #结束请求

        #检查data是否为空数据,可以使用print(data)查看数据结构
        if len(data) >= 3:
            packet_id = data[0][0]
            if packet_id == 255:
                status = "在线"
                protocol = data[1].decode('utf-8', 'ignore')
                version = data[2].decode('utf-8', 'ignore')
                title = data[3].decode('utf-8', 'ignore')
                numplayers = data[4].decode('utf-8', 'ignore')
                maxplayers = data[5].decode('utf-8', 'ignore')
                smode=True
            else:
                status = "未知状态"
                smode=False
        else:
            status = "未知状态"
            smode=False

        return status,protocol,version,title,numplayers,maxplayers,smode

    except Exception as e:
        print("Error:", e)
        return "离线","\000","\000","\000","\000","\000",smode

class timebox():
    def gettime():
        _,__,___,hour,minute,____,_____,______,_______ = loadtime()
        return hour,minute
    
    def outputtimebox():
        year,month,day,hour,minute,sea,_____,______,_______ = loadtime()
        return f'[{year}/{month}/{day} {hour}:{minute}:{sea}]'


def Easytosend(emails,content=''):
    sender = 'xxx@xxx.com' #用户名与发送方
    receivers = ['xxx@xxx.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    cc_mail=emails #抄送人
    subject = f'{timebox.outputtimebox()} 土豆风控-PotatoRiskControl'
    # 口令,QQ邮箱是输入授权码
    mail_pass = "xxx"
    file=''
    image=''
    SendMail(sender,receivers,cc_mail,mail_pass,content,file,image,subject)


def clear():
    os.system('clear' if os.name == 'posix' else 'cls') 
    print("\033[H\033[J", end='')

def better_print(input_str:str,delay:float=0.01,end:str='\n'):  
    for char in input_str:  
        print(char, end='', flush=True)
        time.sleep(delay)
    print(end=end)

def print_fancy(text:str, color=Fore.WHITE, background=Back.RESET):  
    """  
    打印带有颜色和背景色的文本。  
      
    :param text: 要打印的文本  
    :param color: 文本颜色（默认为白色）  
    :param background: 背景色（默认为无）  
    """  
    print(f"{background}{color}{text}{Style.RESET_ALL}")  