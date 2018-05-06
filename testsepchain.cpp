#include "project.h"

int main() {
  SepChain sc;
  string keys[] = {"k", "kieran", "ryker", "kiernan", "r", "reichurr", "bob"};
    string vals[] = {"kieran", "ryker", "kiernan", "reichurr", "rayyan", "q", "kie"};
    for (int n = 0; n < 7; n++) {
      sc.insert(keys[n], vals[n]);
    }
    for (int n = 0; n < 6; n++) {
      Entry s = sc.search(keys[n]);
      if (s == EMPTY) {
	cout << "Error: " << keys[n] << " not found in table!" << endl;
	return 1;
      }
    }

    sc.dump(std::cout, DUMP_KEY_VALUE);
    return 0;
}
