import requests  
from bs4 import BeautifulSoup  

def fetch_and_extract_messages(url:str):  
    try:  
        # 发送HTTP GET请求  
        response = requests.get(url)  
          
        # 确保请求成功  
        response.raise_for_status()  
          
        # 使用BeautifulSoup解析HTML  
        soup = BeautifulSoup(response.text, 'html.parser')  
          
        # 找到所有的<p>标签  
        p_tags = soup.find_all('p')  
          
        # 提取每个<p>标签的文本内容并存储在列表中  
        messages = [p.get_text(strip=True) for p in p_tags]  
          
        # 返回提取的消息列表  
        return messages
    except requests.RequestException as e:  
        print(f"请求错误: {e}")  
        return []  

  
def potatoget():
    url = 'https://www.potatocraft.top/PotatoRiskControlSystem/message.html'  
    return fetch_and_extract_messages(url)
