#include<iostream>
#include<conio.h>
using namespace std;
void display(int value){
	cout<<"Integer value:"<<value<<endl;
}
void display (float value){
	cout<<"Float value:"<<value<<endl;

}
void display(char value){
	cout<<"Character value:"<<value<<endl;
}
int main(){
	int i=10;
	float f=3.14;
	char c='S';
	display(i);
	display(f);
	display(c);
	return 0;
}