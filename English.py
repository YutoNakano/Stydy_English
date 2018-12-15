from collections import Counter
import re

# Englishファイル作成


# English.textの中身の英語の文章から一番使われている英単語、上位1000個抽出
words = re.findall(r'\w+', open('English.text').read().lower())
Counter(words).most_common(1000)


# コマンド　＋ め でコメントアウト便利
