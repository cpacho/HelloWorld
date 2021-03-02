#! /usr/bin/env python
import rospy
from stdmsgs.msg import String

def talker():
  pub = rospy.Publisher('miprimertopicenROS', String, queuesize=10)
  rospy.initnode('talker', anonymous=True)
  rate = rospy.Rate(10) #10 hz
  while not rospy.isshutdown():
    hellostr="Hola grupo de robotica %s" %rospy.gettime()
    rospy.loginfo(hellostr)
    pub.publish(hellostr)
    rate.sleep()
ifname == 'main':
  try:
    talker()
  except rospy.ROSInterruptException:
    pass
