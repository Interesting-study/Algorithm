#https://www.acmicpc.net/problem/3613
import re

def convert_cpp(match):
    value = '_'+match.group().lower()
    return value

def covert_java(match):
    value = match.group()[1:].title()
    return value

val = input()

java_convert_pattern = re.compile(r'[A-Z][a-z]*')
cpp_convert_pattern = re.compile(r'[_][a-z]*')

java_valid_pattern = re.compile(r'^[a-z]+([A-Z][a-z]*)*$')
cpp_valid_pattern = re.compile(r'^[a-z]+(_[a-z]+)*$')

if java_valid_pattern.match(val):#java 패턴일 때
    answer = java_convert_pattern.sub(convert_cpp, val)
    print(answer)
elif cpp_valid_pattern.match(val):#c패턴일 때
    answer = cpp_convert_pattern.sub(covert_java, val)
    print(answer)
else:
    print("Error!")

