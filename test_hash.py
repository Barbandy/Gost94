﻿#coding: UTF-8
import subprocess
import pytest
import gost94

def run_cmd(cmd, input=None):
    pr = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    return pr.communicate(input=input)


def hash_gost94(text):
    cmd_line= ['openssl', 'dgst', '-hex', '-md_gost94']
    out, err = run_cmd(cmd_line, input=text)
    if err:
        raise ValueError('OpenSSL error: %s' % err)
    # (stdin)= hash /n
    out = out[9:-1]
    return out	


def test_gost94():
    data = 'test'
    assert  hash_gost94(data) == gost94.calc_gost94(data)
    


	