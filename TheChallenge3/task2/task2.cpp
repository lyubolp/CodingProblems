#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>
#include <map>
#include <queue>
#include <unordered_set>

typedef std::vector<std::vector<int>> graph;
typedef std::vector<int> isomorphic_f;

graph initialize_new(const int size) { //O(N)
    graph result;
    
    for (int i = 0; i <= size; i++) {
        result.push_back(std::vector<int>());
    }

    return result;

}

graph handle_input(const int n) {
    graph result = initialize_new(n); //O(N)

    for (int current_point = 1; current_point < n; current_point++) { //O(N^2)
        int amount_of_points = 0;
        std::cin >> amount_of_points;

        int point = 0;
        for (int j = 0; j < amount_of_points; j++) {
            std::cin >> point;
            result[current_point].push_back(point);
        }
    }

    return result;
}

void display_graph(const graph& board) {
    for (int i = 1; i < board.size(); i++) { 
        std::cout << i << ": ";
        for (int j = 0; j < board[i].size(); j++) {
            std::cout << board[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

graph map_graph(const graph& graph_to_be_mapped, const isomorphic_f& mapping) { //O(N^2)
    graph mapped_graph = initialize_new(graph_to_be_mapped.size() - 1); //O(N)

    for (int old_index = 1; old_index < graph_to_be_mapped.size(); old_index++) { //O(N^2)
        int new_index = mapping[old_index-1];

        for (auto old_neighbour: graph_to_be_mapped[old_index]) {
            mapped_graph[new_index].push_back(mapping[old_neighbour-1]);
        }
    }

    return mapped_graph;
}

bool are_graphs_isomorphic(const graph& mapped_graph1, const graph& graph2) { //O(N^2)
    for (int i = 1; i < mapped_graph1.size(); i++) {
        if (mapped_graph1[i].size() != graph2[i].size()) {
            return false;
        }

        for (int j = 0; j < graph2[i].size(); j++) {
            if (mapped_graph1[i][j] != graph2[i][j]) {
                return false;
            }
        }
    }

    return true;
}

void display_isomorphic_mapping_result(const isomorphic_f& mapping, int n) { 
    for (int i = 1; i < n; i++) {
        std::cout << mapping[i-1] << " ";
    }
    std::cout << mapping[n-1];
}

graph generate_possible_mappings(const graph& first, const graph& second, const std::map<int, int>& levels_graph1, const std::map<int, int>& levels_graph2) {
    int n = first.size();
    graph result = initialize_new(n);

    result[1].push_back(1);
    result[n].push_back(n);

    for (int i = 2; i < n; i++) {
        for(int j = 2; j < n; j++) {
            if (first[i].size() == second[j].size() && levels_graph1.find(i)->second == levels_graph2.find(j)->second) {
                result[i].push_back(j);
            }
        }
    }

    return result;
}

isomorphic_f find_mapping(const graph& mappings, const graph& graph_1, const graph& graph_2) {
    std::stack<std::pair<std::vector<int>, std::unordered_set<int>>> stack;
    std::unordered_set<std::string> visited;

    stack.push({{1}, {1}});

    while (!stack.empty()) {
        std::pair<std::vector<int>, std::unordered_set<int>> item = stack.top();
        
        std::vector<int> current_mapping = item.first;
        std::unordered_set<int> current_mapping_set = item.second;

        stack.pop();

        if (current_mapping.size() == mappings.size() - 1) {
            std::string str_version="";

            for (auto item: current_mapping) {
                str_version += (std::to_string(item) + ",");
            }

            auto search = visited.find(str_version);

            if (search == visited.end()) {
                graph mapped_graph = map_graph(graph_1, current_mapping);

                if (are_graphs_isomorphic(mapped_graph, graph_2)) {
                    return current_mapping;
                }
                visited.insert(str_version);
            }
        }

        for(auto item: mappings[current_mapping.size()+1]) {

            auto search = current_mapping_set.find(item);

            if (search == current_mapping_set.end()) {
                current_mapping.push_back(item);
                current_mapping_set.insert(item);

                stack.push({current_mapping, current_mapping_set});
                
                current_mapping.pop_back();
                current_mapping_set.erase(item);
            }   
        }
    }

    isomorphic_f def;

    for(int i = 0; i <= graph_1.size(); i++) {
        def.push_back(i);
    }
    return def;
}

std::map<int, int> bfs(const graph& graph) {
    std::queue<std::pair<int, int>> queue;
    queue.push({1, 0});

    std::unordered_set<int> visited;

    std::map<int, int> result;
    while (!queue.empty()) {
        std::pair<int, int> current = queue.front();

        int current_node = current.first;
        int current_level = current.second;
        
        queue.pop();

        if (visited.find(current_node) != visited.end()) {
            continue;
        }

        auto finder = result.find(current_node);

        if (finder == result.end()) {
            result.insert({current_node, current_level});
        }
        
        visited.insert(current_node);
        for(int neightbour: graph[current_node]) {
            queue.push({neightbour, current_level + 1});
        }
    }

    return result;
}

int main() {
    int n;
    std::cin >> n;

    graph first = handle_input(n);
    graph second = handle_input(n);

    graph mappings = generate_possible_mappings(first, second, bfs(first), bfs(second));
    isomorphic_f result = find_mapping(mappings, first, second);

    display_isomorphic_mapping_result(result, n);

    return 0;   
}