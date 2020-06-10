#!/usr/bin/env python

def validate_username(username, length):
    assert type(username) == str, "username should be string"
    if length < 1:
        raise ValueError("Length can not be less than 1")
    if len(username) < length:
        return False
    if not username.isalnum():
        return False
    else:
        return True
