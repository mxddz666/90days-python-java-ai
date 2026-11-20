# 速查表

## Python 常用

```python
# 列表推导式
[x * 2 for x in range(10) if x % 2 == 0]

# 字典遍历
for k, v in d.items():
    print(k, v)

# 异常处理
try:
    ...
except ValueError as e:
    ...
finally:
    ...

# 上下文管理
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()
```

## Java 常用

```java
// 集合遍历
for (String s : list) { System.out.println(s); }

// Stream 过滤排序
list.stream().filter(x -> x > 80).sorted().collect(Collectors.toList());

// try-with-resources
try (BufferedReader br = Files.newBufferedReader(path)) {
    ...
}

// Lambda
Runnable r = () -> System.out.println("hello");
```

## PyTorch 训练循环

```python
for x, y in loader:
    optimizer.zero_grad()
    pred = model(x)
    loss = loss_fn(pred, y)
    loss.backward()
    optimizer.step()
```

## sklearn 标准流程

```python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = Pipeline([("scaler", StandardScaler()), ("model", LogisticRegression())])
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
```

## Git 常用

```bash
git status
git add .
git commit -m "Day 01 完成"
git push origin main
```
