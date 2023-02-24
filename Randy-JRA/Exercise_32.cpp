//Challenge 32 is to Create a function that will capitalize the first letter of each word in a text 
#include <iostream>
#include <string>
#include <cctype>
 
void toUpper(std::string &str) {
    if (str.length() == 0) {
        return;
    }
 
    str[0] = std::toupper(str[0]);
}
 
int main()
{
    std::string str = "stay cool feel free knowledge a gift";
 
    toUpper(str);
    std::cout << str << std::endl;       
 
    return 0;
}

