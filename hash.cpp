#include "project.h"

int main() {
	string password;
	while (cin >> password) {
		unsigned long long hash = 83;
		for (size_t i = 0; i < password.size(); i++) {
			hash = (hash * 38921) ^ (93179 * (password[i] - 8));
		}
		//if (hash < 0) hash = -hash;
		cout << hash << endl;
	}
	return 0;
}
