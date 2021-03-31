#ifndef _INCLUDE_ASCIIREADER_H
#define _INCLUDE_ASCIIREADER_H

#include "Framework.h"

class AsciiReader 
{
    // Global vars and functions.
    public:
        std::string outTxt;
        void readFile(std::string file);
};

#endif //_INCLUDE_ASCIIREADER_H