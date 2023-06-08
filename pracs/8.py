def main(text):
    tmp_text = text
    tmp_text = tmp_text.replace("\n", "")
    dic = {}
    key = ""
    value = ""
    for i in range(len(tmp_text)):
        if tmp_text.startswith("glob") == 0:
            tmp_text = tmp_text[1:]
        else:
            tmp_text = tmp_text[4:]
            if tmp_text[0] == " ":
                tmp_text = tmp_text[1:]
            while tmp_text[0] not in " :":
                key += tmp_text[0]
                tmp_text = tmp_text[1:]
            while tmp_text[0] not in "-0123456789":
                tmp_text = tmp_text[1:]
            while tmp_text[0] not in " ]":
                value += tmp_text[0]
                tmp_text = tmp_text[1:]
            dic.update({key: int(value)})
            key = ""
            value = ""
    return (dic)
