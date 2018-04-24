#include "project.h"

int main() {
	Trie t;
	string keys[] = {"k", "kieran", "ryker", "kiernan", "r", "reichurr", "bob"};
	for (int n = 0; n < 7; n++) {
		t.insert(keys[n]);
	}
	string vals[] = {"kieran", "ryker", "kiernan", "reichurr", "rayyan", "q", "kie", "crayon", "ryker", "fuck", "k", "r"};
	for (int n = 0; n < 12; n++) {
		bool s = t.search(vals[n]);
		cout << s << endl;
	}
	
	return 0;
}
