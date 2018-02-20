import matplotlib as mpl
import matplotlib.pyplot as plt
data = []
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = "hello, my friend. how do you do?"

for i in range(len(abc)):
    count = 0
    for j in text:
        if (j == abc[i]):
                count += 1
    data.append(count)
    print("%s - %s" % (abc[i], count))
print(data)
print(len(data))

dpi = 100
fig = plt.figure(dpi = dpi, figsize = (600 / dpi, 400 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.title('hello, my friend. how do you do?')

ax = plt.axes()

xs = range(len(abc))
plt.bar([x + 0.0 for x in xs],  data,
          color = 'blue', alpha = 0.8,
         zorder = 0)
plt.xticks(xs, abc, rotation =10)
plt.show()
