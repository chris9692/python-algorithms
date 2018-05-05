def _generate(str, pairs, opens, closes):
    if closes == 0:
        print(str)
        return
    if opens < closes:
        _generate(str + ')', pairs, opens, closes - 1)
    if opens > 0:
        _generate(str + '(', pairs, opens - 1, closes)

def generate(pairs):
    _generate('', pairs, pairs, pairs)

    
class ParenthesisCombinations(object):
    """
    This class provides a mechanism to generate N pairs of
    parentheses, all possible combinations
    """
    @classmethod
    def generate(cls, pairs):
        if pairs < 1:
            return None
        elif pairs == 1:
            return ['()']
        else:
            combinations = []
            basepairs = cls.generate(pairs-1)
            print(basepairs)
            for b in basepairs:
                for i in range(len(b)):
                    combinations.append(b[0:i+1]+'()'+b[i+1:])
            return list(set([c for c in combinations]))
