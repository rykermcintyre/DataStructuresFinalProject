// project.h

#pragma once

#include <iostream>
#include <string>
#include <vector>

using namespace std;

// TrieNode struct

struct TrieNode {
	char letter;
	bool terminal;
	vector<TrieNode*> children;
};

// Trie

class Trie {
public:
	void insert(const string word);
	bool search(const string word);
private:
	TrieNode root;
};
