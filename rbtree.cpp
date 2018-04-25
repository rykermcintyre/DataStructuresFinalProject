// rbtree.cpp

#include "project.h"

RBTree::RBTree () {}

RBTree::~RBTree () {}

void RBTree::insert(const string &key, const string &value){
    entries[key] = value;
}

const Entry RBTree::search(const string &key){
    auto result = entries.find(key);
    if (result == entries.end()) return EMPTY;
    else return *result;
}

void RBTree::dump(ostream &os, DumpFlag flag){
    for (auto it = entries.begin(); it != entries.end(); it++){
        switch (flag){
            case DUMP_KEY:
                os << it->first << endl; 
                break;
            case DUMP_VALUE:
                os << it->second << endl;
                break;
            case DUMP_KEY_VALUE:
                os << it->first << "\t" << it->second << endl;
                break;
            case DUMP_VALUE_KEY:
                os << it->second << "\t" << it->first << endl;
                break;
        }
    }
}
