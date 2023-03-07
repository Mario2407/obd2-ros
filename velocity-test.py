import rclpy
from rclpy.node import Node
import obd
import time
from std_msgs.msg import Float64
import re

rclpy.init()
node = rclpy.create_node('my_publisher')
pub_vel = node.create_publisher(Float64, 'vel', 10)

connection = obd.Async()

def new_rpm(r):
    print (r.value)
    match = re.search(r'\d+.\d+', str(r.value))
    pub_vel.publish(Float64(data=float(match.group())))

connection.watch(obd.commands.SPEED, callback=new_rpm)
connection.start()
rclpy.spin(node)
connection.stop()
