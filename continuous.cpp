#include "project.h"
#include <iostream>
#include <string>

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
	while (true) {
		string user, pass, signal;
		cin >> signal;
		if (signal == "insert") {
			cin >> user >> pass;
			r.insert(user, pass);
			t.insert(user);
		}
		else if (signal == "find") {
			cin >> user >> pass;
			if (!t.search(user)) {
				cout << "nouser\n";
			}
			else {
				if (r.search(user).second == pass) {
					cout << "success\n";
				}
				else {
					cout << "incorrect\n";
				}
			}
		}
	}
}

void linkedlist() {
	List r;
	Trie t;
	while (true) {
		string user, pass, signal;
		cin >> signal;
		if (signal == "insert") {
			cin >> user >> pass;
			r.push_back(user, pass);
			t.insert(user);
		}
		else if (signal == "find") {
			cin >> user >> pass;
			if (!t.search(user)) {
				cout << "nouser\n";
			}
			else {
				if (r.search(user) == pass) {
					cout << "success\n";
				}
				else {
					cout << "incorrect\n";
				}
			}
		}
	}
}

void sepchain() {
	SepChain r;
	Trie t;
	while (true) {
		string user, pass, signal;
		cin >> signal;
		if (signal == "insert") {
			cin >> user >> pass;
			r.insert(user, pass);
			t.insert(user);
		}
		else if (signal == "find") {
			cin >> user >> pass;
			if (!t.search(user)) {
				cout << "nouser\n";
			}
			else {
				if (r.search(user).second == pass) {
					cout << "success\n";
				}
				else {
					cout << "incorrect\n";
				}
			}
		}
	}
}
