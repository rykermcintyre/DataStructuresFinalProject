#include "project.h"

int main() {
	Trie t;
	string keys[] = {"kieran", "ryker", "kiernan", "reichurr"};
	for (int n = 0; n < 4; n++) {
		t.insert(keys[n]);
	}
	string vals[] = {"kieran", "ryker", "kiernan", "reichurr", "rayyan", "q", "kie", "crayon", "fuck"};
	for (int n = 0; n < 9; n++) {
		bool s = t.search(vals[n]);
		cout << s << endl;
	}
	
	return 0;
}
