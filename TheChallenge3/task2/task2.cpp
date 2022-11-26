#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>
#include <map>

typedef std::vector<std::vector<int>> graph;
typedef std::map<int, int> isomorphic_f;

graph initialize_new(const int size) {
    graph result;
    
    for (int i = 0; i <= size; i++) {
        result.push_back(std::vector<int>());
    }

    return result;

}

graph handle_input(const int n) {
    graph result = initialize_new(n);

    for (int current_point = 1; current_point < n; current_point++) {
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

graph map_graph(const graph& graph_to_be_mapped, const isomorphic_f& mapping) {
    graph mapped_graph = initialize_new(graph_to_be_mapped.size() - 1);

    for (int old_index = 1; old_index < graph_to_be_mapped.size(); old_index++) {
        int new_index = mapping.find(old_index)->second;

        for (auto old_neighbour: graph_to_be_mapped[old_index]) {
            mapped_graph[new_index].push_back(mapping.find(old_neighbour)->second);
        }
    }

    return mapped_graph;
}

bool are_graphs_isomorphic(const graph& mapped_graph1, const graph& graph2) {
    for (int i = 1; i < mapped_graph1.size(); i++) {
        if (mapped_graph1[i].size() != graph2[i].size()) {
            return false;
        }

        for (int j = 0; j < mapped_graph1[i].size(); j++) {
            if (mapped_graph1[i][j] != graph2[i][j]) {
                return false;
            }
        }
    }

    return true;
}

isomorphic_f get_next_isomorphic_mapping(const isomorphic_f& mapping) { 

    std::vector<int> current_mapping;
    for (auto it: mapping) {
        current_mapping.push_back(it.second);
    }

    std::next_permutation(current_mapping.begin(), current_mapping.end());

    isomorphic_f result;

    for(int i = 1; i <= current_mapping.size(); i++) { 
        result.insert({i, current_mapping[i-1]});
    }

    return result;
}

void display_isomorphic_mapping(const isomorphic_f& mapping) {
    for(auto it: mapping) {
        std::cout << "{" << it.first << ", " << it.second << "}" << std::endl;
    }
}

void display_isomorphic_mapping_result(const isomorphic_f& mapping, int n) { 
    for (int i = 1; i < n; i++) {
        std::cout << mapping.find(i)->second << " ";
    }
    std::cout << mapping.find(n)->second;
}

isomorphic_f dfs(const graph& graph_1, const graph& graph_2, const int n, bool is_showing_debug_info = false) {
    isomorphic_f first_mapping;

    for (int i = 1; i <= n; i++) {
        first_mapping.insert({i, i});
    }


    std::stack<isomorphic_f> stack;
    stack.emplace(first_mapping);

    while (!stack.empty()) {
        isomorphic_f current_mapping = stack.top();


        stack.pop();

        graph mapped_graph = map_graph(graph_1, current_mapping);
        
        
        if (are_graphs_isomorphic(mapped_graph, graph_2)) {
            return current_mapping;
        }
        else {
            stack.emplace(get_next_isomorphic_mapping(current_mapping));
        }

        if (is_showing_debug_info) {
            std::cout << "--start--\n";
            
            std::cout << "Mapping: " << std::endl;
            display_isomorphic_mapping(current_mapping);
            std::cout << std::endl;
            std::cout << "Original graph: " << std::endl;
            display_graph(graph_1);

            std::cout << "Mapped graph: " << std::endl;
            display_graph(mapped_graph);

            std::cout << "Target graph: " << std::endl;
            display_graph(graph_2);
            
            std::cout << "--end--\n";
        
        }
    }

    return isomorphic_f();
}
int main() {
    int n;
    std::cin >> n;

    graph first = handle_input(n);
    graph second = handle_input(n);

    // std::cout << "First:" << std::endl;
    // display_graph(first);

    // std::cout << "Second:" << std::endl;
    // display_graph(second);


    isomorphic_f result = dfs(first, second, n, false);

    display_isomorphic_mapping_result(result, n);
    
    return 0;   
}