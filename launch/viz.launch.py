import launch
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    image_topic = LaunchConfiguration("image_topic")
    detection_topic = LaunchConfiguration("detection_topic")

    image_topic_arg = DeclareLaunchArgument(
        "image_topic", default_value="/camera1/camera/color/image_raw", description="Input image topic"
    )

    detection_topic_arg = DeclareLaunchArgument(
        "detection_topic", default_value="/detections", description="AprilTag detections topic"
    )

    composable_node = ComposableNode(
        name="apriltag_viz",
        package="apriltag_viz",
        plugin="AprilVizNode",
        remappings=[
            ("image", image_topic),
            ("detections", detection_topic),
        ],
    )
    container = ComposableNodeContainer(
        name="viz_container",
        namespace="apriltag",
        package="rclcpp_components",
        executable="component_container",
        composable_node_descriptions=[composable_node],
        output="screen",
    )

    return launch.LaunchDescription([image_topic_arg, detection_topic_arg, container])
