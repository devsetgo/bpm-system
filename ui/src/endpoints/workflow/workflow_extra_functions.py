# -*- coding: utf-8 -*-
"""
    Common functions for the workflow engine and associated processing
"""
import shortuuid
from datetime import date
import uuid

# from core.crud_ops import execute_one_db, fetch_one_db

from unsync import unsync


def generate_business_key(identifier: str = None, key: str = None) -> str:
    """
    Generate a business key for a new workflow instance
    """
    year = date.today().year
    dayofyear = date.today().timetuple().tm_yday
    u = uuid.uuid4()

    alphabet = "abcdefghijklmnopqrstuvxyz1234567890"
    if identifier is None:
        identifier = "CASE"
    if key is None:
        key = shortuuid.ShortUUID().random(length=10)
    return f"{identifier}-{year:.-2}{dayofyear}|{key}"


def check_for_duplicates(dup_list: list):
    """
    Check for duplicate entries in a list
    """
    from collections import Counter

    c = Counter(dup_list).most_common(2)
    print(c)


if __name__ == "__main__":
    from tqdm import tqdm

    dup_list: list = []

    for _ in tqdm(range(1000000)):
        dup_list.append(generate_business_key())
    # print(type(dup_list))
    check_for_duplicates(dup_list)
