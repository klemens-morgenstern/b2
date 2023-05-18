#!/usr/bin/env python3

# Copyright 2023 Klemens Morgenstern 

import BoostBuild

t = BoostBuild.Tester()

t.write("jamroot.jam", """
import openssl ;
exe test-openssl : test-openssl.cpp : requirements <library>/openssl//ssl ;
# <library>/openssl//ssl 
""")

t.write("test-openssl.cpp", 
"""
#include <openssl/ssl.h>

int main() 
{
  SSL_load_error_strings(); 
  SSL_library_init();
  return 0;
}
""")


t.run_build_system(["link=shared"])
t.run_build_system(["link=static"])

t.cleanup()
