def delete(s):
    if not s:
        return
    res = []
    for i in s:
        if i not in res:
            res.append(i)

    return ''.join(res)


s = "google"
print(delete(s))
