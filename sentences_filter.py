import sentence_process as p

def remove_sims(text: str):
    text = text.split('.')
    ret = text.copy()
    for i in range(len(text)):
        if text[i] not in ret:
            continue
        for j in range(i + 1, len(text)):
            if text[j] not in ret:
                continue
            if p.calculate_similarity(text[i], text[j]) > 0.6:
                ret.remove(text[j])
    return '.'.join(ret)


