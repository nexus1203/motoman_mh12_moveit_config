import rospy
from std_srvs.srv import Trigger

def enable_robot():
    rospy.wait_for_service('/robot_enable')
    try:
        enable_robot_service = rospy.ServiceProxy('/robot_enable', Trigger)
        response = enable_robot_service()  # std_srvs/Trigger has empty request
        return response.success, response.message
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

if __name__ == "__main__":
    rospy.init_node('robot_enabler')
    success, message = enable_robot()
    print(f"Success: {success}, Message: {message}")
