#include "project.h"

int main() {
	RBTree rb;
	string keys[] = {"k", "kieran", "ryker", "kiernan", "r", "reichurr", "bob"};
    string vals[] = {"kieran", "ryker", "kiernan", "reichurr", "rayyan", "q", "kie", "crayon", "ryker", "fuck", "k", "r"};
	for (int n = 0; n < 7; n++) {
		rb.insert(keys[n], vals[n]);
	}
	for (int n = 0; n < 12; n++) {
		Entry s = rb.search(keys[n]);
		rb.dump(std::cout, DUMP_KEY_VALUE);
	}
	
	return 0;
}
