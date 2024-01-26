#include <iostream>
#include <iomanip>

int main() {
   
    double A, B, C, media;
    std::cin >> A >> B >> C;
    media = (A * 2 + B * 3 + C * 5) / 10;
    
    std::cout << std::fixed << std::setprecision(1);
    std::cout <<"MEDIA = " << media << std::endl;
    return 0;

}
