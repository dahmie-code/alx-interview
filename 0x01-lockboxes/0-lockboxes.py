#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you. Each box is numbered sequentially 
    from 0 to n - 1 and each box may contain keys to the other boxes. 
    """
    firstBox = [0]
    for key in firstBox:
        for keyBox in boxes[key]:
            if keyBox not in firstBox:
                if keyBox < len(boxes):
                    firstBox.append(keyBox)
    if len(firstBox) == len(boxes):
        return True
    return False