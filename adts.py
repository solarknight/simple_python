# list
weekdays = ['Monday', 'Tuesday', 'Wednesday']

weekdays.append('Thursday')

print(weekdays[0])
print(weekdays[-1])

weekdays.insert(0, 'Friday')
weekdays.insert(-1, 'Saturday')
print(weekdays[0])
print(weekdays[-2])

weekdays[0:0] = ['Sunday']
print(weekdays)

del weekdays[0:2]
print(weekdays)

nums = [4, 2, 3, 1]
print(sorted(nums))
print(sorted(nums, reverse = True))

for a, b in zip(weekdays, nums):
    print(a, 'and', b)

nums = [i * 2 for i in range(0, 4)]
print(nums)

nums = [i ** 2 for i in range(0, 4)]
print(nums)

for idx, num in enumerate(nums):
    print('Index', idx, 'is', num)

# dict
upper_str = {
    "google": "GOOGLE",
    "baidu": "BAIDU",
    "sogou": "SOGOU"
}

print(upper_str["google"])

upper_str["yahoo"] = "YAHOO"
print(upper_str["yahoo"])

del upper_str["baidu"]
print(upper_str)

num_char = {i:j for i,j in zip(range(1, 6), 'abcde')}
print(num_char)

# tuple
letters = ('a', 'b', 'c', 'd', 'e')
print(letters[0])

# set
char_set = {'a', 'b', 'c'}
char_set.add('d')
char_set.add('c')
print(char_set)
