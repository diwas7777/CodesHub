#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <cmath>
#include <utility>

struct RegisterResult {
    std::string status;
    std::vector<std::pair<std::string, double>> change;
};

long long toCents(double amount) {
    return static_cast<long long>(std::llround(amount * 100.0));
}

double fromCents(long long cents) {
    return static_cast<double>(cents) / 100.0;
}

RegisterResult checkCashRegister(double price, double cash,
                                 const std::vector<std::pair<std::string, double>>& cid) {
    const std::vector<std::pair<std::string, long long>> denominations = {
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

    const long long priceCents = toCents(price);
    const long long cashCents = toCents(cash);
    const long long requiredChange = cashCents - priceCents;

    if (requiredChange < 0) {
        return {"INSUFFICIENT_FUNDS", {}};
    }

    long long drawerTotal = 0;
    std::vector<std::pair<std::string, long long>> drawerInCents;

    for (const auto& item : cid) {
        const long long amount = toCents(item.second);
        drawerInCents.push_back({item.first, amount});
        drawerTotal += amount;
    }

    if (drawerTotal < requiredChange) {
        return {"INSUFFICIENT_FUNDS", {}};
    }

    if (requiredChange == 0) {
        return {"OPEN", {}};
    }

    if (drawerTotal == requiredChange) {
        return {"CLOSED", cid};
    }

    std::vector<std::pair<std::string, double>> resultChange;
    long long remainingChange = requiredChange;

    for (size_t i = 0; i < denominations.size(); ++i) {
        const auto& [name, value] = denominations[i];
        long long available = drawerInCents[i].second;
        long long used = 0;

        while (remainingChange >= value && available > 0) {
            remainingChange -= value;
            available -= value;
            used += value;
        }

        if (used > 0) {
            resultChange.push_back({name, fromCents(used)});
        }
    }

    if (remainingChange > 0) {
        return {"INSUFFICIENT_FUNDS", {}};
    }

    return {"OPEN", resultChange};
}

int main() {
    const std::vector<std::pair<std::string, double>> drawer = {
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

    RegisterResult result = checkCashRegister(19.50, 20.00, drawer);

    std::cout << "Status: " << result.status << "\n";
    std::cout << "Change:\n";
    for (const auto& item : result.change) {
        std::cout << "  - " << item.first << ": $"
                  << std::fixed << std::setprecision(2) << item.second << "\n";
    }

    return 0;
}
