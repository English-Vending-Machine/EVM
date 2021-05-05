# 순서 문제 지문 완벽화
def type_order(text, answer):

    first_english = False
    C_chunk = False
    temp_str = ""
    alphabet = ''
    paren = ''
    chunk = []
    perfect_text = ""
    index = 0

    """    
    # 문제에서 시작 문장, A,B,C 지문 chunk 추출하여 chunk에 저장.
    while index < len(text):
        if ord('a') <= ord(text[index].lower()) <= ord('z'):
            first_english = True
        if first_english:
            if text[index] == '(':
                alphabet = text[index + 1]
                paren = text[index + 2]
                if alphabet == 'A' and paren == ')':
                    print(temp_str)
                    chunk.append(temp_str)
                    temp_str = ""
                    index += 3
                    continue
                elif (alphabet == 'B' and paren == ')'):
                    chunk.append(temp_str)
                    temp_str = ""
                    index += 3
                    continue
                elif (alphabet == 'C' and paren == ')'):
                    chunk.append(temp_str)
                    temp_str = ""
                    index += 3
                    C_chunk = True
                    continue
            elif text[index] == '\n':
                if (C_chunk):
                    if (text[index + 1] == '\n'):
                        break
                index += 1
                continue
            temp_str += text[index]
            first_english = True
        index += 1
    chunk.append(temp_str)

    # 시작 문장 insert
    pefect_text = chunk[0]
    # A-C-B
    if answer == 1:
        perfect_text += chunk[1]
        perfect_text += chunk[3]
        perfect_text += chunk[2]
    # B-A-C
    elif answer == 2:
        perfect_text += chunk[2]
        perfect_text += chunk[1]
        perfect_text += chunk[3]
    # B-C-A
    elif answer == 3:
        perfect_text += chunk[2]
        perfect_text += chunk[3]
        perfect_text += chunk[1]
    # C-A-B
    elif answer == 4:
        perfect_text += chunk[3]
        perfect_text += chunk[1]
        perfect_text += chunk[2]
    # C-B-A
    elif answer == 5:
        perfect_text += chunk[3]
        perfect_text += chunk[2]
        perfect_text += chunk[1]

    return perfect_text"""
    return text