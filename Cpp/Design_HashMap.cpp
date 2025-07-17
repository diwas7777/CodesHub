class MyHashMap {
public:
    int arr[1000001];
    MyHashMap() {
        fill(arr, arr + 1000000, -1); // initalizing with -1.
    }
    void put(int key, int val) {
        arr[key] = val;
    }
    int get(int key) {
        return arr[key];
    }
    void remove(int key) {
        arr[key] = -1;
    }
};
/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */
