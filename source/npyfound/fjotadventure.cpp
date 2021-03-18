#include <iostream>

int main()
{
    const char prompt = '\t>';
    std::string title = "||||||||||||||      |||VVVVVVVV|||     \n"
                        "|||                 |||        |||     \n"
                        "||||||||||||||      |||VVVVVVVV|||     \n"
                        "|||                 |||        |||     \n"
                        "|||                 |||        |||     \n"
                        "|||                 |||        |||     \n"
                        "|||                 |||        |||     \n"
                        "|||                 |||        |||     \n"
                        "|||             o   |||        |||   o \n";
    std::string input;
    std::cout<<title; 
    std::cout<<"Pick a character to start.\n[1] Shidneka\n[2]Bghays\n";
    std::cout<<prompt;
    std::cin>>input;
    return 0;
}
