#include "project.h"
#include <iostream>
#include <string>
#include <ctime>

using namespace std;

void rbtree();
void linkedlist();
void sepchain();

int main() {
	string mode;
	cin >> mode;
	
	if (mode == "rbtree") rbtree();
	else if (mode == "linkedlist") linkedlist();
	else if (mode == "sepchain") sepchain();
	
	return 0;
}

void rbtree() {
	RBTree r;
	Trie t;
	clock_t start;
	clock_t end;
	clock_t diff;
	while (true) {
		string user, pass, signal;
		cin >> signal;
		if (signal == "insert") {
			cin >> user >> pass;
			if (!t.search(user)) {
				start = clock();
				r.insert(user, pass);
				end = clock();
				diff = (end - start);
				t.insert(user);
				cout << "inserted\n";
				cout << diff << endl;
			}
			else {
				cout << "exists\n";
				cout << "-\n";
			}
		}
		else if (signal == "find") {
			cin >> user >> pass;
			if (!t.search(user)) {
				cout << "nouser\n";
				cout << "-\n";
			}
			else {
				start = clock();
				if (r.search(user).second == pass) {
					end = clock();
					cout << "success\n";
				}
				else {
					end = clock();
					cout << "incorrect\n";
				}
				diff = (end - start);
				cout << diff << endl;
			}
		}
	}
}

void linkedlist() {
	List r;
	Trie t;
	clock_t start;
	clock_t end;
	clock_t diff;
	while (true) {
		string user, pass, signal;
		cin >> signal;
		if (signal == "insert") {
			cin >> user >> pass;
			if (!t.search(user)) {
				start = clock();
				r.push_back(user, pass);
				end = clock();
				diff = (end - start);
				t.insert(user);
				cout << "inserted\n";
				cout << diff << endl;
			}
			else {
				cout << "exists\n";
				cout << "-\n";
			}
		}
		else if (signal == "find") {
			cin >> user >> pass;
			if (!t.search(user)) {
				cout << "nouser\n";
				cout << "-\n";
			}
			else {
				start = clock();
				if (r.search(user) == pass) {
					end = clock();
					cout << "success\n";
				}
				else {
					end = clock();
					cout << "incorrect\n";
				}
				diff = (end - start);
				cout << diff << endl;
			}
		}
	}
}

void sepchain() {
	SepChain r;
	Trie t;
	clock_t start;
	clock_t end;
	clock_t diff;
	while (true) {
		string user, pass, signal;
		cin >> signal;
		if (signal == "insert") {
			cin >> user >> pass;
			if (!t.search(user)) {
				start = clock();
				r.insert(user, pass);
				end = clock();
				diff = (end - start);
				t.insert(user);
				cout << "inserted\n";
				cout << diff << endl;
			}
			else {
				cout << "exists\n";
				cout << "-\n";
			}
		}
		else if (signal == "find") {
			cin >> user >> pass;
			if (!t.search(user)) {
				cout << "nouser\n";
				cout << "-\n";
			}
			else {
				start = clock();
				if (r.search(user).second == pass) {
					end = clock();
					cout << "success\n";
				}
				else {
					end = clock();
					cout << "incorrect\n";
				}
				diff = (end - start);
				cout << diff << endl;
			}
		}
	}
}
