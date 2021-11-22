* 2차원 배열 뒤집기
  * scores = list(map(list, zip(*scores)))

<br>

* 리스트의 *
  * "원소 원소" 식으로 출력됨
  

<br>

* 문제에 접근할 때
  * 수식화 할 수 있는가?
  * 단순화 할 수 없는가?
  * 그림으로 그려볼 순 없는가?
  * 수식으로 표현할 수 있는가?
  * 문제를 분해랄 수 있는가?
  * 뒤에서부터 생각할 수 있는가?
  * 순서를 강제할 수 있는가?
  * 특정 형태의 답만 고려할 수 있는가?


<br>

* 약수 구하기(효율적)
~~~ 
def get_divisor(n):
    divisors = []
    divisore_reverse = []

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if (i != (n // i)):
                divisore_reverse.append(n // i)

    return divisors + divisore_reverse[::-1]
~~~



<br>

* n진수 구하기(재귀함수)
~~~
def convert(n, base):
    base_str = '0123456789ABCDEF'
    q, r = divmod(n, base)

    if q == 0:
        return base_str[r]
    else:
        return convert(q, base) + base_str[r]
~~~
