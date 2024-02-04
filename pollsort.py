def inbetween(text:"str", start:"str", end:"str") -> str:
    start_index = text.find(start) + len(start)
    end_index = text.find(end, start_index)
    if start_index == -1 or end_index == -1:
        return None
    value = text[start_index:end_index]
    return value