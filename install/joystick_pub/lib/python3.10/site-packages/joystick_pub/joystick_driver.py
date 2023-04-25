# coding:utf-8
import pygame
import socket
import time


ip = '192.168.32.137'
#ip = '127.0.0.1'
port = 9999
# 创建连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def test_func():
  # [event type] [轴/按键的索引] [value_1] 
  value_1 = float(0)
  index = int(0)
  s.sendto(bytes(("Button" + "," + str(index) + "," + str(value_1) ), encoding="utf-8"), (ip, port))
  time.sleep(1)
  value_1 = 0.5
  s.sendto(bytes(("Axis" + "," + str(index) + "," + str(value_1) ), encoding="utf-8"), (ip, port))
  time.sleep(1)
  value_1 = 0
  s.sendto(bytes(("Left" + "," + str(index) + "," + str(value_1) ), encoding="utf-8"), (ip, port))
  time.sleep(1)
  s.sendto(bytes(("Right" + "," + str(index) + "," + str(value_1) ), encoding="utf-8"), (ip, port))
  time.sleep(1)
  s.sendto(bytes(("Down" + "," + str(index) + "," + str(value_1) ), encoding="utf-8"), (ip, port))
  time.sleep(1)
  s.sendto(bytes(("Up" + "," + str(index) + "," + str(value_1) ), encoding="utf-8"), (ip, port))
  s.close()
  exit(0)


# test_func()



def main():
  # 模块初始化
  pygame.init()
  pygame.joystick.init()

  # 若只连接了一个手柄，此处带入的参数一般都是0
  joystick = pygame.joystick.Joystick(0)
  # 手柄对象初始化
  joystick.init()

  buttons = joystick.get_numbuttons()
  axes = joystick.get_numaxes()
  hats = joystick.get_numhats()
  
  print("axes number:",axes)
  print("buttons number:",buttons)
  print("hats number:",hats)

  done = False
  while not done:
    try:
      for event_ in pygame.event.get():
        # 退出事件
        if event_.type == pygame.QUIT:
          done = True
        # 按键按下
        elif event_.type == pygame.JOYBUTTONDOWN:
          # 获取所有按键状态信息
          value_1 = float(0)
          for i in range(buttons):
            button = joystick.get_button(i)
            if button:
              s.sendto(bytes(("Button" + "," + str(i) + "," + str(value_1)), encoding="utf-8"), (ip, port))
        # 弹起事件
        # elif event_.type == pygame.JOYBUTTONUP:
        #   # 获取所有按键状态信息
        #   for i in range(buttons):
        #     button = joystick.get_button(i)
        #     if button:
        #       s.sendto(bytes(("Button" + "," + str(i) + "," + str(value_1)), encoding="utf-8"), (ip, port))
        # 轴转动事件
        elif event_.type == pygame.JOYAXISMOTION:
          # 获取所有轴状态信息
          value_1 = float(0)
          # for i in range(axes):
          # -1.0 到 1.0
          axis = joystick.get_axis(0)
          value_1 = axis
          s.sendto(bytes(("Axis" + "," + str(0) + "," + str(value_1)), encoding="utf-8"), (ip, port))
          # 方向键改变事件
        elif event_.type == pygame.JOYHATMOTION:
          value_1 = float(0)
          # 获取所有方向键状态信息
          for i in range(hats):
            hat = joystick.get_hat(i)
            if hat[0] == -1:
              s.sendto(bytes(("Left" + "," + str(i)+ "," + str(value_1)),encoding="utf-8"),(ip, port))
            if hat[0] == 1:
              s.sendto(bytes(("Right"+ "," + str(i) + "," + str(value_1)),encoding="utf-8"),(ip, port))
            if hat[1] == -1:
              s.sendto(bytes(("Down"+ "," + str(i) + "," + str(value_1)),encoding="utf-8"),(ip, port))
            if hat[1] == 1:
              s.sendto(bytes(("Up"+ "," + str(i) + "," + str(value_1)),encoding="utf-8"),(ip, port))
    except KeyboardInterrupt:
      print ('KeyboardInterrupt exception is caught')
      break

  pygame.quit()
  s.sendto(b'exit', (ip, port))

  s.close()
  
if __name__ == '__main__':
  main()

