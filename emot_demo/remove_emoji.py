import re
from emoji import demojize


def remove_emoji_by_re(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F" # emoticons
                           u"\U0001F300-\U0001F5FF" # symbols & pictographs
                           u"\U0001F680-\U0001F6FF" # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF" # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


def remove_emoji(string):
    # 字符串中的: 会影响识别颜文字部分
    temp = demojize(string)
    print(f"demojize: {temp}")
    return re.sub(r':\S+?:', '', temp)

def main():
    # 根据 unicode 范围来删除表情符号、通用的和IOS中的，不是很全，也没找到非常全的list
    # 还是有些过滤不掉
    text = "Nice app:‑🤭 I like it"
    print(f"Before: {text}")
    print(f"After: {remove_emoji_by_re(text)}")
    print(f"After: {remove_emoji(text)}")

    text = "Hilarious 😂! The feeling of making a sale 😎, The feeling of actually fulfilling orders 😒"
    print(f"Before: {text}")
    print(f"After: {remove_emoji_by_re(text)}")
    print(f"After: {remove_emoji(text)}")

if __name__ == '__main__':
    main()

