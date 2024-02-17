cmake_minimum_required(VERSION 3.20)

project(cprogram)

set(SOURCE_FILES src/lib.c)

add_library(cprogram SHARED ${SOURCE_FILES})

target_include_directories(cprogram PRIVATE include)

set_target_properties(cprogram PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/lib
)
