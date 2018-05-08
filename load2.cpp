#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int main(int argc, char *argv[]) {
  string a = argv[1];
  string cmd = "python2 userGen2.py " + a + " >> database.txt";
  system("rm database.txt");
  system(cmd.c_str());
  return 0;
}
