import threading  
import curses  
import time 
import arts

def draw_picture(stdscr, color_pair,lists):  
    # 假设图案存储在字符串列表中    
    height, width = stdscr.getmaxyx()  
    center_x = width // 2  
    center_y = height // 2 - len(lists) // 2  
      
    for y, line in enumerate(lists):  
        # 居中显示 
        stdscr.addstr(center_y + y, center_x - len(line) // 2, line, curses.color_pair(color_pair))  
  
def gui(stdscr):  
    index=0
    curses.curs_set(0)  # 隐藏光标
    stdscr.nodelay(1) # 设置非阻塞模式   
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)    # 霓虹红  
    while True:  
        # 清除屏幕  
        stdscr.clear()  
        # 选择颜色对  
        color_pair = 1
        #获取
        pt,mode=arts.guireturn(index)
        # 绘制
        draw_picture(stdscr, color_pair,pt)  
        # 刷新屏幕  
        stdscr.refresh()  
        # 等待一小段时间  
        time.sleep(0.05)  
        #动画索引
        index += 1
        if index>18:index=0

        if mode:
            # 监听退出键  
            try:
                if stdscr.getch() == ord('s'):  
                    break  
            except curses.error:
                pass


def play():
    curses.wrapper(gui)

def main():
    loading_thread = threading.Thread(target=arts.getandreturn)  
    fetch_thread = threading.Thread(target=play)

    loading_thread.start()  
    fetch_thread.start()   

if __name__ == '__main__':
    # play()
    main()