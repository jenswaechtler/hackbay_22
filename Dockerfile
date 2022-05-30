FROM osrf/ros:galactic-desktop

# using bash
SHELL ["/bin/bash", "-c"]

RUN apt-get update

RUN mkdir -p /home/ws/src
COPY . /home/ws/src/camer

# RUN sudo rosdep init
RUN rosdep update

RUN cd /home/ws \
    && source /opt/ros/galactic/setup.bash \
    && rosdep install \
                    -y -r --from-paths src \
                    --ignore-src --rosdistro=galactic 

RUN source /opt/ros/galactic/setup.bash \
    && cd /home/ws \
    && colcon build

CMD source /opt/ros/galactic/setup.bash \
     && source /home/ws/install/setup.bash \
     ros2 run usb_cam usb_cam_node_exe
