import sys

def longest_prefix_suffix():
    s = sys.stdin.read().strip()

    if not s:
        return
    
    n = len(s)
    pi = [0] * n

    for i in range (1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j

    print(f'Answer is: {pi[n - 1]}')
    # word = slice(0, pi[n - 1])
    # print(f'The longest prefix-suffix: {s[word]}')

if __name__ == '__main__':
    longest_prefix_suffix()
