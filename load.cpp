#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
  system("rm database.txt");
  system("python2 userGen.py 1000 >> database.txt");
  return 0;
}
