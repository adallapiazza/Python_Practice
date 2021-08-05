# test for palindrome

test = "test"
palindrome = "tacocat"

t = []
for c in test:
    t.append(c)
print(t)
print(t[::-1])
print(t == t[::-1])
print()

p = []
for c in palindrome:
    p.append(c)
print(p)
print(p[::-1])
print(p == p[::-1])

def pal_test(word):
    w = []
    sent = "".join(e for e in word if e.isalpha())
    for c in sent:
        w.append(c)
    print(w == w[::-1])

pal_test("alex")
pal_test("drawkward")
pal_test("dr.awkward")
