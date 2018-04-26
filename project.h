// project.h

#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <functional>
using namespace std;

typedef enum {
    DUMP_KEY,
    DUMP_VALUE,
    DUMP_KEY_VALUE,
    DUMP_VALUE_KEY,
} DumpFlag;
typedef pair<string, string> Entry;
extern const Entry NONE;
const pair<string, string> EMPTY ("NULL", "NULL");

typedef std::hash<std::string> HashFunky;

extern const double DEFAULT_LOAD_FACTOR;
extern const size_t DEFAULT_TABLE_SIZE;

// TrieNode struct

struct TrieNode {
	char letter;
	bool terminal;
	vector<TrieNode*> children;
};

// RBTree struct
struct RBTreeNode{
    int data;
    bool color;
    RBTreeNode *left;
    RBTreeNode *right;
    RBTreeNode *parent;
    RBTreeNode(int data){
        this->data = data;
        left = NULL;
        right = NULL;
        parent = NULL;
    }
};

struct Node {
    Entry data;
    Node *next;
};

class Trie {
public:
    Trie();
    ~Trie();
    void insert(const string word);
    bool search(const string word);
    bool deconstruct(TrieNode *node);
private:
    TrieNode root;
};

class Map {
public:
    virtual void        insert(string &key, string &value) {}
    virtual const Entry search(string &key) { return EMPTY; }
    virtual void        dump(ostream &os, DumpFlag flag) {}
};

class RBTree : public Map {
public:
    RBTree();
    ~RBTree();
    void        insert(const string &key, const string &value);
    const Entry search(const string &key);
    void        dump(ostream &os, DumpFlag flag);
private:
    map<string, string> entries;
};

class List {
private:
    typedef Node *iterator;
    //Node *head;
    size_t length;
public:
    Node *head;
    List() : head(nullptr), length(0) {}
    iterator front() { return head; }
    ~List();
    size_t size() const { return length; }
    void push_back(const string username, const string password);
    void erase(iterator it);
    string search(const string username);
};

class SepChain : public Map {
 public:
  void insert(const string &key, const string &value);
  const Entry search(const string &key);
  void dump(ostream &os, DumpFlag flag);
  SepChain(size_t table_size = DEFAULT_TABLE_SIZE, double load_factor = DEFAULT_LOAD_FACTOR) {
    tsize = table_size;
    lfactor = load_factor;
    table = new map<string, string>[tsize];
    counter = 0;
  };

  ~SepChain() {
    delete [] table;
  }

 private:
  void resize(const size_t new_size);
  map<string, string> *table;
  HashFunky funky;
  size_t tsize;
  size_t lfactor;
  size_t counter;
};
