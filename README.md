# motoman_mh12_moveit_config
Moveit config for Motoman MH12 robot in ROS Noetic and Moveit 1.

Build the package with motoman_driver in catkin_ws

Start Rviz with following command: (robot_ip is the ip of the DX200 controller)

`roslaunch motoman_mh12_moveit_config moveit_planning_execution.launch robot_ip:=192.168.1.2 sim:=false`

To enable the robot run:

`rosservice call /robot_enable`

To disable the robot run:

`rosservice call /robot_disable`
