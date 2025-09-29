def sort_on(entry):
    return entry['num']

def get_word_count(text: str) -> int:
    return len(text.split())

def get_character_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for char in text:
        lc = char.lower()
        counts[lc] = counts.get(lc, 0) + 1
    return counts

def get_sorted_dict(counts: dict[str, int]):
    entries = [{'char': ch, 'num': n} for ch, n in counts.items()]
    entries.sort(reverse=True, key=sort_on)
    return entries