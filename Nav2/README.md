# Navigation 2
https://navigation.ros.org/setup_guides/index.html

## Transformation
TF2 assumes all transformation goes from parent to child. Typically base_link is the parent. Use URDF to store info on robot structure. To obtain relative position `ros2 run tf2_ros tf2_echo base_link base_laser`

## URDF