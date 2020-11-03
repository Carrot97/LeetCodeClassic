"""
Given an array of n distinct non-empty strings, you need to generate minimal
possible abbreviations for every word following rules below.Begin with the
first character and then the number of characters abbreviated, which followed
by the last character.If there are any conflict, that is more than one words
share the same abbreviation, a longer prefix is used instead of only the first
character until making the map from word to abbreviation become unique.
In other words, a final abbreviation cannot map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.

Example:
Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
"""


# 参考 http://bookshadow.com/weblog/2017/03/12/leetcode-word-abbreviation/
def wordsAbbreviation(dict):
    ans = {}

    def get_abbr(word, prefix):
        if len(word) - prefix <= 2:
            return word
        return word[:prefix] + str(len(word) - prefix - 1) + word[-1]

    def helper(dict, prefix):
        voc = {}
        for word in dict:
            abbr = get_abbr(word, prefix)
            if abbr not in voc:
                voc[abbr] = [word]
            else:
                voc[abbr].append(word)
        for abbr, words in voc.items():
            if len(words) == 1:
                ans[words[0]] = abbr
            else:
                helper(words, prefix + 1)

    helper(dict, 1)
    return list(map(lambda word: ans[word], dict))


print(wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]))
