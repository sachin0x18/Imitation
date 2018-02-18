# Imitation
ROS-Kinetic Package that facilitates imitation of Human actions by Humanoid (built using Dynamixel Servos). Human actions are recorded by Kinect sensor.

Using vector geometry and quaternions, coordinates of human joints are published. Using these coordinates, servo angles are written to Dynamixel servos thus imitating human actions in real time.

# SLAM
SLAM (Simultaneous Localization And Mapping) is also implemented using the rtabmap_ros package that uses Kinect sensor rgb images and depth sensor thus creating a 3D point cloud as well as 2D occupancy grid

Publishing Kinect data
> $ roslaunch freenect_launch freenect.launch depth_registration:=true

Visualizing and generating map using
1)	rtabmap 
>	 $ roslaunch rtabmap_ros rtabmap.launch rtabmap_args:=" 	delete_db_on_start"

OR
 
2) rviz
>	$ roslaunch rtabmap_ros rtabmap.launch rtabmap_args:="--delete_db_on_start" rviz:=true rtabmapviz:=false
