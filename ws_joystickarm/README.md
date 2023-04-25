
# 主要代码工作目录
	~/ws_joystickarm/src
	.
	├── joystick_pub
	│   ├── joystick_pub
	│   ├── package.xml
	│   ├── resource
	│   ├── setup.cfg
	│   ├── setup.py
	│   └── test
	└── realtime_servo
			├── CMakeLists.txt
			├── config
			├── launch
			├── package.xml
			├── realtime_servo_tutorial.rst
			├── servo_rqt_graph.png
			└── src

	8 directories, 7 files


# 执行步骤

## 1.进入工作目录
	cd ~/ws_joystickarm

## 2.使能当前设置（打开一个新终端就要执行一次）
	. install/setup.bash

## 3.启动手柄驱动
	cd ~/ws_joystickarm
	ros2 run joystick_pub joystick_driver


## 4.新建终端，启动ros2 moveit2指令发布程序
	cd ~/ws_joystickarm
	ros2 run joystick_pub joystick_pub


## 5.新建终端，启动moveit2的机械手臂
	cd ~/ws_joystickarm
	sh launch.sh



# 编译代码
	cd ~/ws_joystickarm
	sh build.sh

# IP设置
ip在joystick_pub.py和joystick_driver.py修改对应的IP地址


# ws_moveit2目录
 路径为~/ws_moveit2，改目录是编译的moveit2包，不能删除，否则无法启动moveit2