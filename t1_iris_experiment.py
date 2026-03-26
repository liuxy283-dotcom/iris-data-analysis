import math
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("鸢尾花数据分析")

# 读取数据
X = []
y = []

with open('iris.data', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            parts = line.split(',')
            row = []
            for p in parts[:4]:
                if p == 'Null' or p == '':
                    row.append(float('nan'))
                else:
                    row.append(float(p))
            X.append(row)
            y.append(parts[4])

print("样本数:", len(X))
print("特征数:", len(X[0]))
feature_names = ['花萼长度', '花萼宽度', '花瓣长度', '花瓣宽度']

# 缺失值处理
n = len(X)
m = 4
missing = 0
for i in range(n):
    for j in range(m):
        if math.isnan(X[i][j]):
            missing += 1

print("缺失值数量:", missing)

for j in range(m):
    col = [X[i][j] for i in range(n) if not math.isnan(X[i][j])]
    mean_val = sum(col) / len(col)
    for i in range(n):
        if math.isnan(X[i][j]):
            X[i][j] = mean_val
print("缺失值已填充")

# 归一化
means = []
stds = []
for j in range(m):
    col = [X[i][j] for i in range(n)]
    mean_val = sum(col) / n
    means.append(mean_val)
    var = sum((x - mean_val) ** 2 for x in col) / n
    std_val = math.sqrt(var)
    stds.append(std_val)
    for i in range(n):
        if std_val != 0:
            X[i][j] = (X[i][j] - mean_val) / std_val
print("归一化完成")

# 统计

for j in range(m):
    col = sorted([X[i][j] for i in range(n)])
    mean_val = sum(col) / n
    if n % 2 == 0:
        median = (col[n//2] + col[n//2 - 1]) / 2
    else:
        median = col[n//2]
    var = sum((x - mean_val) ** 2 for x in col) / n

    print(feature_names[j])
    print("均值:", round(mean_val, 3))
    print("中位数:", round(median, 3))
    print("方差:", round(var, 3))
    print()

# 可视化
plt.figure(figsize=(12, 4))
# 直方图
plt.subplot(1, 3, 1)
for j in range(m):
    col = [X[i][j] for i in range(n)]
    plt.hist(col, alpha=0.5, label=feature_names[j])

plt.title("直方图")
plt.legend()

# 散点图
plt.subplot(1, 3, 2)
for i in range(n):
    plt.scatter(X[i][0], X[i][1])

plt.xlabel("花萼长度")
plt.ylabel("花萼宽度")
plt.title("散点图")

# 箱线图
plt.subplot(1, 3, 3)
data_box = []
for j in range(m):
    col = [X[i][j] for i in range(n)]
    data_box.append(col)

plt.boxplot(data_box, labels=feature_names)
plt.title("箱线图")
plt.tight_layout()
plt.show()
# 6. 分析
print("\n分析：")
print("花瓣相关特征变化比较明显，区分度更高")
print("不同类别在某些特征上差异较大")
