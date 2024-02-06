from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os.path

def generate_launch_description():

    # rviz_config_file = PathJoinSubstitution(
    #     [FindPackageShare("ag1_bringup"), "rviz2", "ag1_odom.rviz"]
    # )

    teleop_node = Node(
        package="teleop_twist_keyboard",
        executable="teleop_twist_keyboard",
        parameters=[],
        remappings=[
             ('/cmd_vel', '/diffbot_base_controller/cmd_vel_unstamped'),
            ],
        prefix = 'xterm -e'
    )
    rviz2_node = Node(
            package='rviz2',
            namespace='',
            executable='rviz2',
            name='rviz2',
            # arguments=['-d', rviz_config_file]
            arguments=['-d', "/home/bdigney/ros2_roboclaw/src/ag1_bringup/rviz2/ag1_odom.rviz"]
        )
    nodes = [teleop_node, 
         rviz2_node,      
    ]
    return LaunchDescription(nodes)