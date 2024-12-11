#include <iostream>
#include <iomanip> // Para controlar a precisão de casas decimais

int main() {
    const double PI = 3.14159;
    double raio, area;

    std::cin >> raio;

    area = PI * raio * raio;

    std::cout << std::fixed << std::setprecision(4);
    std::cout << "A=" << area << std::endl;

    return 0;
}
