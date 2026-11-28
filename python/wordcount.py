# 输入一句话，统计单词数并逐个输出
sentence = input("输入一句话：")

# split() 不带参数：按任意空白切分，自动忽略连续空格
words = sentence.split()

print(f"单词数：{len(words)}")
for i, word in enumerate(words, 1):
    print(f"{i}. {word}")
