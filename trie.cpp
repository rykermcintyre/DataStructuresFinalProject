// trie.cpp

#include "project.h"

Trie::Trie() {
	root.letter = '\0';
	root.terminal = false;
	root.children = vector<TrieNode*> (36, nullptr);
}

void Trie::insert(const string word) {
	TrieNode *crawl = &root;
	
	for (int i = 0; i < word.length(); i++) {
		int index;
		if (word[i] >= 48 && word[i] <= 57) index = word[i] - '0';
		else index = word[i] - 'a' + 10;
		
		for (int j = 0; j < crawl->children.size(); j++) {
			if (crawl->children[i]) cout << crawl->children[i];
		}
		
		if (!crawl->children[index]) crawl->children[index] = new TrieNode {.letter = word[i], .terminal = false, .children = vector<TrieNode*> (36, nullptr)};
		
		crawl = crawl->children[index];
	}
	
	crawl->terminal = true;
}

bool Trie::search(const string word) {
	TrieNode *crawl = &root;
	
	for (int i = 0; i < word.length(); i++) {
		int index;
		if (word[i] >= 48 && word[i] <= 57) index = word[i] - '0';
		else index = word[i] - 'a' + 10;
		
		if (!crawl->children[index]) return false;
		
		crawl = crawl->children[index];
	}
	
	return crawl->terminal;
}

bool Trie::deconstruct(TrieNode* node) {
	for (int i = 0; i < 36; i++) {
		if (node->children[i]) deconstruct(node->children[i]);
	}
	delete node;
	return true;
}

Trie::~Trie() {
	for (int i = 0; i < 36; i++) {
		if (root.children[i]) deconstruct(root.children[i]);
	}
}

