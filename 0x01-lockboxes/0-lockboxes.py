#!/usr/bin/python3
"""
A module containing code for working with lockboxes
"""


def canUnlockAll(boxes):
    """
    Checks if all boxes in a list of boxes containing the keys
    to other boxes can be unlocked given the first box is already
    unlocked
    """
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        box_id = unseen_boxes.pop()
        if not box_id or box_id >= n or box_id < 0:
            continue
        if box_id not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[box_id])
            seen_boxes.add(box_id)

    return n == len(seen_boxes)
