class Solution:
    def toGoatLatin(self, S: str) -> str:
        return ' '.join([(lambda w: w[1:]+w[0] if w[0] not in 'aeiouAEIOU' else w)(w) + 'ma' + 'a' * i for i, w in enumerate(S.split(' '), 1)])
