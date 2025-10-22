import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    composable_node = ComposableNode(name='apriltag_viz', package='apriltag_viz', plugin='AprilVizNode')
    container = ComposableNodeContainer(
            name='viz_container',
            namespace='apriltag',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[composable_node],
            remappings=[("/apriltag/image", "/camera/image")],
            output='screen'
    )

    return launch.LaunchDescription([container])