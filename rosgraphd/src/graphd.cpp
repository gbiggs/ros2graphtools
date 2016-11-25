// Copyright 2016 Open Source Robotics Foundation, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <rclcpp/rclcpp.hpp>
#include <rcl/graph.h>

void print_topic_names_and_types(rcl_topic_names_and_types_t* topics)
{
  for(size_t ii = 0; ii < topics->topic_count; ++ii) {
    std::cout << "Topic " << ii << ": " << topics->topic_names[ii] << "<"
              << topics->type_names[ii] << ">\n";
  }
}


int main(int argc, char** argv)
{
  rclcpp::init(argc, argv);

  auto node = rclcpp::Node::make_shared("graphd");
  auto ge = node->get_graph_event();

  while(rclcpp::ok()) {
    node->wait_for_graph_change(ge, std::chrono::seconds(1));
    if (!ge->check_and_clear()) {
      continue;
    }
    auto topics = rcl_get_zero_initialized_topic_names_and_types();
    std::cout << "Getting topic info\n";
    auto ret = rcl_get_topic_names_and_types(node->get_rcl_node_handle(), &topics);
    if (ret != RCL_RET_OK) {
      std::cerr << "Failed to get topic names and types: " << ret << '\n';
      return 1;
    }
    print_topic_names_and_types(&topics);
    rcl_destroy_topic_names_and_types(&topics);
  }

  return 0;
}
