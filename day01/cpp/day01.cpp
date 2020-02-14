#include <iostream>
#include <string>
#include <fstream> 
using namespace std; 
 
int getAnswer(int mass){
	if(mass<0)
		return 0;
	int fuel = (mass/3)-2;
	return fuel + getAnswer(fuel);
} 

int main() 
{ 
    fstream file; 
    string word, filename;
    filename = "input.txt"; 

    // PART 1
    file.open(filename.c_str());  
    int answer = 0;
    while (file >> word) 
        answer += (stoi(word)/3)-2;
    cout<<answer<<endl; 

    // PART 2
    int answer2=0;
    file.clear();
	file.seekg(0, ios::beg);
    while(file>>word)
    	answer2 += getAnswer(stoi(word));
    cout<<answer2<<endl;
    file.close();
   return 0; 
 }
