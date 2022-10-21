class MyHashSet {
public:
        vector<bool> ans;
    MyHashSet() {
        ans.resize(1e6+1,false);
    }

    void add(int key) {
        ans[key]=true;
    }

    void remove(int key) {
        ans[key]=false;
    }

    bool contains(int key) {
        return ans[key];
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
