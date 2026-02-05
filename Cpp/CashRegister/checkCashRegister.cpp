#include <bits/stdc++.h>
using namespace std;

/*
  Cash Register — Greedy Change
  checkCashRegister(price, cash, cid) -> {status, change}

  - price, cash in dollars (double) are converted to integer cents
  - cid: vector of pairs {denomination name, amount in dollars}
  - status: "OPEN" | "CLOSED" | "INSUFFICIENT_FUNDS"
  - change: vector of {denomination, amount} in dollars

  Denominations used:
    "ONE HUNDRED" 100.00
    "TWENTY"        20.00
    "TEN"           10.00
    "FIVE"           5.00
    "ONE"            1.00
    "QUARTER"        0.25
    "DIME"           0.10
    "NICKEL"         0.05
    "PENNY"          0.01
*/

static const vector<pair<string,int>> DENOMS = {
    {"ONE HUNDRED", 10000},
    {"TWENTY", 2000},
    {"TEN", 1000},
    {"FIVE", 500},
    {"ONE", 100},
    {"QUARTER", 25},
    {"DIME", 10},
    {"NICKEL", 5},
    {"PENNY", 1}
};

struct Result {
    string status;
    vector<pair<string,double>> change; // in dollars
};

static int toCents(double d) {
    return (int) llround(d * 100.0);
}

Result checkCashRegister(double price, double cash, const vector<pair<string,double>>& cid) {
    int due = toCents(cash) - toCents(price);

    // Map drawer amounts by denom (in cents)
    unordered_map<string,int> drawer;
    int totalInDrawer = 0;
    for (auto &p : cid) {
        int cents = toCents(p.second);
        drawer[p.first] = cents;
        totalInDrawer += cents;
    }

    if (due > totalInDrawer) {
        return {"INSUFFICIENT_FUNDS", {}};
    }

    vector<pair<string,double>> changeOut;
    int remaining = due;

    for (auto &d : DENOMS) {
        const string& name = d.first;
        int denom = d.second;
        int take = 0;

        int available = drawer.count(name) ? drawer[name] : 0;

        while (remaining >= denom && available >= denom) {
            remaining -= denom;
            available -= denom;
            take += denom;
        }

        // commit
        if (take > 0) {
            changeOut.push_back({name, take / 100.0});
        }
        drawer[name] = available;
    }

    if (remaining != 0) {
        return {"INSUFFICIENT_FUNDS", {}};
    }

    // If we used everything in the drawer
    int left = 0;
    for (auto &p : drawer) left += p.second;
    if (left == 0) {
        // CLOSED: return original cid ordering
        vector<pair<string,double>> closedChange;
        for (auto &p : cid) {
            if (toCents(p.second) > 0)
                closedChange.push_back({p.first, p.second});
        }
        return {"CLOSED", closedChange};
    }

    return {"OPEN", changeOut};
}

int main() {
    vector<pair<string,double>> cid1 = {
        {"PENNY", 1.01},
        {"NICKEL", 2.05},
        {"DIME", 3.10},
        {"QUARTER", 4.25},
        {"ONE", 90.00},
        {"FIVE", 55.00},
        {"TEN", 20.00},
        {"TWENTY", 60.00},
        {"ONE HUNDRED", 100.00}
    };

    auto printRes = [](const Result& r) {
        cout << "status=" << r.status << ", change=[";
        for (size_t i=0;i<r.change.size();++i) {
            cout << "[" << r.change[i].first << "," << fixed << setprecision(2) << r.change[i].second << "]";
            if (i+1<r.change.size()) cout << ",";
        }
        cout << "]\\n";
    };

    cout << "Case 1 (OPEN): ";
    printRes(checkCashRegister(19.50, 20.00, cid1));

    vector<pair<string,double>> cidExact = {{"PENNY", 0.50}};
    cout << "Case 2 (CLOSED): ";
    printRes(checkCashRegister(19.50, 20.00, cidExact));

    vector<pair<string,double>> cidLow = {{"QUARTER", 0.25}};
    cout << "Case 3 (INSUFFICIENT_FUNDS): ";
    printRes(checkCashRegister(19.50, 20.00, cidLow));

    return 0;
}
