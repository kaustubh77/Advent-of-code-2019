#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int intcode(vector<int> a){
    int index =0;
    while(true){
        int opcode = a[index];
        if(opcode == 99)
            return a[0];
        int n1_index = a[index+1];
        int n2_index = a[index+2];
        int ans_index = a[index+3];

        if(opcode == 1)
            a[ans_index] = a[n1_index] + a[n2_index];
        else if(opcode == 2)
            a[ans_index] = a[n1_index] * a[n2_index];
        index+=4;
    }
    return 0;
}

int main()
{
    fstream file;
    string word, filename;
    filename = "input.txt";

    file.open(filename.c_str());

    vector<int> a;
    while((file>>word)!=NULL)
        a.push_back(stoi(word));

    a[1] = 12;
    a[2] = 2;
    cout<<intcode(a)<<endl;
    int answer = 0;
    for(int i=0;i<=99;i++){
        for(int j=0;j<=99;j++){
            a[1] = i;
            a[2] = j;
            if(intcode(a) == 100*i + j){
                answer = intcode(a);
                break;
            }
        }
        if(answer!=0)
            break;
    }
    cout<<answer<<endl;
}