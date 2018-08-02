# -*- coding: utf-8 -*-
# define functions for RSA calculate
# By yanxing

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher
from Crypto.Hash import *
from Crypto.Signature import PKCS1_v1_5 as Signer
from OpenSSL import crypto
from Crypto import Random
import base64
'''
扩展欧几里得算法
'''
def exgcd(a,b,x):
    def exgcd_1(a, b, x):
        if a == 1:
            x[0] = 1
            x[1] = 0
            return
        y = [0, 0]
        exgcd(b % a, a, y)
        x[1] = y[0]
        x[0] = y[1] - b // a * y[0]
        return

    exgcd_1(a,b,x)
    while x[0]<0:
        x[0]=x[0]+b
        x[1]=x[1]-a
    return

'''
RSA密钥的函数
'''
class RsaKey:
    def __init__(self, keylen=1024):
        self._pk=crypto.PKey()
        self._key=self._pk.generate_key(crypto.TYPE_RSA, keylen)
        self._prikey=crypto.dump_privatekey(crypto.FILETYPE_PEM,self._pk)
        self._pubkey=crypto.dump_publickey(crypto.FILETYPE_PEM,self._pk)
        self._KeyLen=self._pk.bits()//8
        return

    def publickey(self):
        return self._pubkey
    '''
    source: 传入的明文，可以bytes,字符串型, 其他类型参数将抛出异常
    '''
    def sign(self,source):
        if type(source) == bytes:
            s1 = source
        elif type(source) == str:
            s1 = source.encode()
        else:
            raise ValueError("source type error")

        h = SHA.new(s1)
        key = RSA.importKey(self._prikey)
        signer = Signer.new(key)
        return signer.sign(h)

    '''
    source: 传入的明文，可以bytes,字符串型, 其他类型参数将抛出异常
    digest: 传入的签名信息，可以bytes,或base64编码的字符串型, 其他类型参数将抛出异常
    pubkey: 用于验证签名的公钥，可以为空，若为空，则使用对象自己的公钥
    '''
    def verify(self,source,digest,pubkey=None):
        if type(source) == bytes:
            s1 = source
        elif type(source) == str:
            s1 = source.encode()
        else:
            raise ValueError("source type error")

        if type(digest) == bytes:
            ct1 = digest
        elif type(digest) == str:
            ct1 = base64.b64decode(digest)
        else:
            raise ValueError("digest type error")

        h = SHA.new(s1)
        if pubkey is None:
            key=RSA.importKey(self._pubkey)
        else:
            key=RSA.importKey(pubkey)
        verifier = Signer.new(key)
        return verifier.verify(h,ct1)

    '''
    source: 传入的明文，可以bytes,字符串型, 其他类型参数将抛出异常
    pubkey: 用于加密的公钥，可以为空，若为空，则使用对象自己的公钥
    '''
    def encrypt(self,source,pubkey=None):
        if type(source) == bytes:
            s1 = source
        elif type(source) == str:
            s1 = source.encode()
        else:
            raise ValueError("source type error")

        if len(s1)<=self._KeyLen:
            if pubkey is None:
                key=RSA.importKey(self._pubkey)
            else:
                key=RSA.importKey(pubkey)
            cryptor=Cipher.new(key)
            return cryptor.encrypt(s1)
        else:
            raise ValueError("source data is too long")


    '''
    ct: 传入的密文，可以bytes,或base64编码的字符串型, 其他类型参数将抛出异常
    '''
    def decrypt(self,ct):
        if type(ct) == bytes:
            ct1 = ct
        elif type(ct) == str:
            ct1 = base64.b64decode(ct)
        else:
            raise ValueError("ct type error")

        if len(ct1)<=self._KeyLen:
            key=RSA.importKey(self._prikey)
            decrypter = Cipher.new(key)
            sentinel = Random.new().read(15 + self._KeyLen )
            return decrypter.decrypt(ct1,sentinel)
        else:
            raise ValueError("source data is to long")



