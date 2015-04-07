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


def hash_gost94(fn):
    '''
    Получение текстового представления хэш-кода переданного текста
    по ГОСТ Р 34.11-94.
    text    текст, хэш-код которого необходимо получить
    return  хэш-код
    '''
    cmd_line = ['rhash', '--gost', fn]

    out, err = run_cmd(cmd_line, input=None)
    if err:
        raise ValueError('Rhash error: %s' % err)
    # Удаляем наименование файла за хешем (..hash..  test)
    out = out[:-7]
    return out	


def test_gost94():
    fn = 'test'
    data = gost94.readFile(fn)
    assert hash_gost94(fn) == gost94.calc_gost94(data)
	
#if __name__ == '__main__':
   # test_gost94()