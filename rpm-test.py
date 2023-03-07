# testing cyclic publishing of rpm from odb2 adapter in ros humble
import rclpy
from rclpy.node import Node
import obd
import time
from std_msgs.msg import Float64
import re

rclpy.init()
node = rclpy.create_node('my_publisher')
pub = node.create_publisher(Float64, 'rpm', 10)

connection = obd.Async()

def new_rpm(r):
    print (r.value)
    match = re.search(r'\d+.\d+', str(r.value))
    pub.publish(Float64(data=float(match.group())))

connection.watch(obd.commands.RPM, callback=new_rpm)
connection.start()
rclpy.spin(node)
connection.stop()
