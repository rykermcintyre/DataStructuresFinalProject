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
    string username;
    string password;
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
    virtual const Entry search(string &key) { return NONE; }
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
public:
    List() : head(nullptr), length(0) {}
    iterator front() { return head; }
    ~List();
    List(const List<string, string> other);
    List<string, string>&operator=(List<string, string> other);
    void swap(List<string, string> &other);
    size_t size() const { return length; }
    T& at(const size_t i);
    void insert(iterator it, const string username, const string password);
    void push_back(const string username, const string password);
    void erase(itertor it);
    bool search(const string username, const string password);
private:
    typedef Node *iterator;
    Node *head;
    size_t length;
};
