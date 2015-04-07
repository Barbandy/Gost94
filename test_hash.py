#coding: UTF-8
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

def get_text_digest(text):
    '''
    Получение текстового представления хэш-кода переданного текста
    по ГОСТ Р 34.11-94.
    @param  text    Текст, хэш-код которого необходимо получить.
    @return Закодированный в base64 хэш-код текста.
    '''
    openssl_sign_cmd = ['openssl', 'dgst', '-binary', '-md_gost94']

    out, err = run_cmd(openssl_sign_cmd, input=text)
    if err:
        raise ValueError('OpenSSL error: %s' % err)

    return out


def test_ripemd160():
    data = 'GOST R 34.11-94'
    assert hash_gost94(data) == gost94.calc_gost94(data)
	
#if __name__ == '__main__':
    #test_ripemd160()
   #data = 'GOST R 34.11-94'
   # print get_text_digest(data)
