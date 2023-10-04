riddle = 'mi1rewopret'

def solve_riddle(riddle:str, word_length:int, start_letter:str, reverse=False) -> str:

    if reverse:
        end_index = riddle.rfind(start_letter)
        if end_index == -1:
            return ''
        start_index = end_index - word_length + 1
        word_reversed = riddle[start_index:end_index + 1]
        res_word = word_reversed[::-1]
        return res_word
    else:
        start_index = riddle.find(start_letter)
        if start_index == -1:
            return ''
        end_index = start_index + word_length
        res_word = riddle[start_index:end_index]
        return res_word

# print(solve_riddle(riddle, 5, 'p', True))
print(solve_riddle(riddle[::-1], 5, 'p', False))