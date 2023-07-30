#include<iostream>
#include<fstream>
#include<vector>
#include<set>
#include<map>
using namespace std;

#define N 100

bool flag=false;
int adj_matrix[N][N] = {0};

bool DFS(int curr, set<int>&wSet, set<int>&gSet, set<int>&bSet) {
   //moving curr to white set to grey set.
   wSet.erase(wSet.find(curr));
   gSet.insert(curr);

   for(int v = 0; v < N; v++) {
      if(adj_matrix[curr][v] != 0) {    //for all neighbour vertices
         if(bSet.find(v) != bSet.end())
            continue;    //if the vertices are in the black set
         if(gSet.find(v) != gSet.end())
            return true;    //it is a cycle
         if(DFS(v, wSet, gSet, bSet))
            return true;    //cycle found
      }
   }

   //moving v to grey set to black set.
   gSet.erase(gSet.find(curr));
   bSet.insert(curr);
   return false;
}

bool hasCycle() {
   set<int> wSet, gSet, bSet;    //three set as white, grey and black
   for(int i = 0; i<N; i++)
      wSet.insert(i);    //initially add all node into the white set

   while(wSet.size() > 0) {
      for(int current = 0; current < N; current++) {
         if(wSet.find(current) != wSet.end())
            if(DFS(current, wSet, gSet, bSet))
               return true;
      }
   }
   return false;
}

int main()
{
    vector<string> line;
    string read;
    ifstream f;
    f.open("input2.txt");
    while(getline(f, read))
    {
        line.push_back(read);
    }
    
    for (int i = 0; i < line.size(); i++)
    {
        for (int j = i + 1; j < line.size(); j++)
        {
            if (line[i][3] == line[j][3])
            {
                if ((line[i][0] == 'r' && line[j][0] == 'w') || (line[i][0] == 'w'))
                {
                    int a = int(line[i][1]) - 49;
                    int b = int(line[j][1]) - 49;
                    
                    if (a != b)
                        adj_matrix[a][b] = 1;
                }
            }
        }
    }
    
    flag=hasCycle();

    (flag)?
        cout << "\nConflict Serialization NOT POSSIBLE\n\n" :
        cout << "\nConflict Serialization POSSIBLE\n\n";
}