# hackbay_22

## Use this package
```bash
mkdir hackbay_ws/src
cd  hackbay_ws/src
git clone ...
cd ../..
colcon build -symlink install
```

```bash
cd hackbay_ws
source install/setup.bash
ros2 run garbage_detection gargarbage_detection_node 
```

## Only for Demo/Test
### 

′′′bash
ros2 run image_tools cam2image --ros-args -p burger_mode:=True
′′′