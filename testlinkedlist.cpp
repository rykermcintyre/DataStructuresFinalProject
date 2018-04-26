#include "project.h"

int main(){
    List l;
    string keys[] = {"kieran", "ryker", "rayyan"};
    string vals[] = {"digiorno", "mcintyre", "karim"};
    for (int n = 0; n < 3; n++){
        l.push_back(keys[n], vals[n]);
    }
    for(auto it = l.head; it != nullptr; it = it->next){
        cout << "Username: " << it->data.first << " Password: " << it->data.second << endl;
    }
    string k;
    k = l.search("kieran");
    cout << "Kieran's password is: " << k << endl;
    string ry;
    ry = l.search("ryker");
    cout << "Ryker's password is: " << ry << endl;
    string ra;
    ra = l.search("rayyan");
    cout << "Rayyan's password is: " << ra << endl;
}
