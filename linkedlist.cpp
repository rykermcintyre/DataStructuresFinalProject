// linkedlist

#include "project.h"

/*List::List() {
    root.username = "";
    root.password = "";
    root->next = nullptr;
}*/

List::~List() {
    Node *next = nullptr;
    for (Node *curr = head; curr != nullptr; curr = next){
        next = curr->next;
        delete curr;
    }
}

void List::push_back(const string username, const string password){
    Entry e = make_pair(username, password);
    if (head == nullptr) head = new Node{e, nullptr};
    else {
        Node *curr = head;
        Node *tail = head;
    
        while (curr){
            tail = curr;
            curr = curr->next;
        }
        tail->next = new Node {e, nullptr};
    }
    length++;
}

void List::erase(iterator it){
    if (it == nullptr){
        throw std::out_of_range("invalid iterator");
    }
    if(head == it){
        head = head->next;
        delete it;
    }
    else {
        Node *node = head;
        while (node != nullptr && node->next != it){
            node = node->next;
        }
        if (node == nullptr) {
            throw std::out_of_range("invalid iterator");
        }
        node->next = it->next;
        delete it;
    }
    length--;
}   

string List::search(const string username){
    if (head == nullptr) return "";
    else {
        Node *curr = head;
        while(curr){
            if(curr->data.first == username) return curr->data.second;
            curr = curr->next;
        }
    }
    return "";
}
