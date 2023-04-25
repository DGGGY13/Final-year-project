import sys
import time 
import socket
import

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from control_msgs.msg import JointJog
from geometry_msgs.msg import TwistStamped



class JoyStickPublisher(Node):
  def __init__(self):
    super().__init__('joystick_publisher')
    ip = '192.168.32.137'
    #ip = '127.0.0.1'
    port = 9999
    # 创建连接
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    
    TWIST_TOPIC = '/servo_node/delta_twist_cmds'
    JOINT_TOPIC = '/servo_node/delta_joint_cmds'
    self.twist_pub_ = self.create_publisher(TwistStamped, TWIST_TOPIC, 1)
    self.joint_pub_ = self.create_publisher(JointJog, JOINT_TOPIC, 1)
    self.get_logger().info(' JoyStickPublisher Bringup')
    self.vel_scale = 1.0
    self.joint_index = 0
    self.panda_joints = ['panda_joint1', 'panda_joint2', 'panda_joint3',
                         'panda_joint4', 'panda_joint5', 'panda_joint6', 'panda_joint7']


  def __del__(self):
    self.socket_server.close()


  def parseCmd(self, data):
    data_list = data.decode('utf-8').split(',')
    cmd = data_list[0]
    index = int(data_list[1])
    data1 = float(data_list[2])

    joint_msg = JointJog()
    # twist_msg = TwistStamped()
    # twist_msg.twist.linear.x = 1.0
    # twist_msg.twist.linear.y = 1.0
    
    publish_joint = False
    vel = float(0.)
    
    if  cmd == 'Button':
      print('cmd',cmd,',index:',index,',data1:',data1)
      self.joint_index = index + 4
      if self.joint_index > 6:
        self.joint_index = 6
    elif  cmd == 'Axis':
      print('cmd',cmd,',index:',index,',data1:',data1)
      # use axis0 to contorl velocity
      if index == 0:
        vel = data1 * self.vel_scale # [-1,1] 
        publish_joint = True
    elif  cmd == 'Left':
      print('cmd',cmd,',index:',index,',data1:',data1)
      self.joint_index = 0
    elif  cmd == 'Right':
      print('cmd',cmd,',index:',index,',data1:',data1)
      self.joint_index = 1
    elif  cmd == 'Down':
      print('cmd',cmd,',index:',index,',data1:',data1)
      self.joint_index = 2
    elif  cmd == 'Up':
      print('cmd',cmd,',index:',index,',data1:',data1)
      self.joint_index = 3
    else:
      publish_joint = False
    
    print("self.joint_index:",self.joint_index,",vel:",vel)
    
    if publish_joint:
      joint_msg.header.stamp = self.get_clock().now().to_msg()
      joint_msg.header.frame_id = 'panda_link0'
      # joint_msg.joint_names.clear()
      joint_msg.joint_names.append(self.panda_joints[self.joint_index])
      # joint_msg.velocities.clear()
      joint_msg.velocities.append(vel)
      # joint_msg.duration = 1.0
      self.joint_pub_.publish(joint_msg)
      publish_joint = False
      print("vel",vel)


  def loop(self):
    s.listen(5)
    print('Waiting for connection...')
    while True:
      try:
        # 无数据接收则线程挂起，等待数据
       
        sock, addr = self.socket_server.accept()
        # print('Received from %s:%s.' % addr)
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()
        if len(data) != 3:
          self.parseCmd(data)
      except KeyboardInterrupt:
        print ('KeyboardInterrupt exception is caught')
        break


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    # 发送数据
    sock.send(b'Welcome!')
    # 接收数据
    while True:
        # 指定最大接收量
        data = sock.recv(1024)
        print data
        if not data or data.decode('utf-8') == 'exit':
            break
    # 关闭Socket
    sock.close()
    print('Connection from %s:%s closed.' % addr)








def main():
  rclpy.init()
  node = JoyStickPublisher()
  node.loop()
  

if __name__ == '__main__':
  main()
