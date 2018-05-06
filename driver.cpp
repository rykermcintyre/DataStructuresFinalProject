#include "project.h"
#include <iostream>
#include <iomanip>
#include <string>
#include <unistd.h>

using namespace std;

void usage(int status) {
  cout << "usage: driver BACKEND USERNAME PASSWORD" << endl;
  return;
}

int main(int argc, char *argv[]) {
  string backend = argv[1];
  string username = argv[2];
  string password = argv[3];
  cout << "BACKEND: " << backend << endl
       << "USERNAME: " << username << endl
       << "PASSWORD: " << password << endl;

  return 0;
}