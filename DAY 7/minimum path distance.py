#include <stdio.h>
#include <limits.h>

#define N 4 // Number of cities

int tsp(int graph[][N], int pos, int visited, int dp[][1 << N]) {
    if (visited == (1 << N) - 1) {
        return graph[pos][0]; // Return to the starting node
    }
    if (dp[pos][visited] != -1) {
        return dp[pos][visited];
    }
    
    int answer = INT_MAX;
    for (int city = 0; city < N; city++) {
        if ((visited & (1 << city)) == 0) {
            int newAnswer = graph[pos][city] + tsp(graph, city, visited | (1 << city), dp);
            answer = (answer < newAnswer) ? answer : newAnswer;
        }
    }
    return dp[pos][visited] = answer;
}

int findMinPath(int graph[][N]) {
    int dp[N][1 << N];
    for (int i = 0; i < N; i++)
        for (int j = 0; j < (1 << N); j++)
            dp[i][j] = -1;

    return tsp(graph, 0, 1, dp);
}

int main() {
    int graph[N][N] = {
        {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0}
    };

    printf("Minimum path distance: %d\n", findMinPath(graph)); // Expected Output: 80

    return 0;
}
