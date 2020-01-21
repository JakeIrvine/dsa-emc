#include <iostream>
#include "sha1.h"

void verifySignature();

void signMessage();

/// Prompts the user to either sign a message or verify a signature.
/// \return true if verify is chosen, false otherwise.
bool selectMode()  {
    char choice;
    while(true) {
        std::cout << "Select mode: \n\t[s] Sign\n\t[v] Verify\n>>> ";

        std::cin >> choice;

        if (choice == 's' || choice == 'v') {
            return choice == 'v';
        }
    }
}

int main() {
    std::cout << "Exeter Maths School DSA Implementation" << std::endl;

    if(selectMode()) { // True if verify mode is chosen
        verifySignature();
    } else {
        signMessage();
    }


    return 0;
}

void signMessage() {

}

void verifySignature() {

}
