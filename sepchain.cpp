#include "project.h"
#include <stdexcept>

void SepChain::insert(const string &key, const string &value) {
  int bucket = funky(key) % tsize;

  Entry match = search(key);

  if (match == EMPTY) {
    counter++;
  }

  table[bucket][key] = value;

  if (lfactor < counter/tsize) {
    resize(tsize * 2);
  }
}

const Entry SepChain::search(const string &key) {
  int bucket = funky(key) % tsize;

  auto match = table[bucket].find(key);
  if (match == table[bucket].end()) {
    return EMPTY;
  }
  else {
    return *match;
  }
}

void SepChain::dump(ostream &os, DumpFlag flag) {
  for (size_t i = 0; i < tsize; i++) {
    for (auto it = table[i].begin(); it != table[i].end(); it++) {
      switch (flag) {
      case DUMP_KEY:          os << it->first  << std::endl; break;
      case DUMP_VALUE:        os << it->second << std::endl; break;
      case DUMP_KEY_VALUE:    os << it->first  << "\t" << it->second << std::endl; \
	break;
      case DUMP_VALUE_KEY:    os << it->second << "\t" << it->first  << std::endl; \
	break;
      }
    }
  }
}

void SepChain::resize(const size_t new_size) {
  map<string, string> *newTable = new map<string, string>[new_size];

  for (size_t i = 0; i < tsize; i++) {
    for (auto it = table[i].begin(); it != table[i].end(); it++) {
      int bucket = funky(it->first) % new_size;
      newTable[bucket][it->first] = it->second;
    }
  }

  delete [] table;

  table = newTable;
  tsize = new_size;
}
