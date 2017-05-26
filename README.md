# STEP17

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [実行方法](#%E5%AE%9F%E8%A1%8C%E6%96%B9%E6%B3%95)
- [関数定義](#%E9%96%A2%E6%95%B0%E5%AE%9A%E7%BE%A9)
  - [予約語](#%E4%BA%88%E7%B4%84%E8%AA%9E)
  - [関数の説明書：docstring](#%E9%96%A2%E6%95%B0%E3%81%AE%E8%AA%AC%E6%98%8E%E6%9B%B8docstring)
- [忘れた頃に見るところ](#%E5%BF%98%E3%82%8C%E3%81%9F%E9%A0%83%E3%81%AB%E8%A6%8B%E3%82%8B%E3%81%A8%E3%81%93%E3%82%8D)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

目次の作成をするには、このREADME.mdがあるディレクトリで `doctoc README.md --github` を実行すれば、自動的に目次を識別して更新してくれる。こちらで消したり加えたりする必要は一切ない。

## 実行方法

|||
|---|----|
|ファイルを実行後、対話型インタープリタに入る|`python -i [filename & arguments]` |
|デバッグ|`python -m pdb [filename & arguments]`|

## 関数定義
### 予約語
### 引数
- 関数名に `*` が入るとき

### 関数の説明書：docstring
```python
def return_asap (anything):
    ''' あたえられた引数をそのまま返す '''
    return anything
```
コマンドラインから実行して、対話型インタープリタに入ったところで、 `help(return_asap)` とすれば、manページのように
説明がでてくる。 `print(return_asap.__doc__)` でもよい。
```
Help on function return_asap in module __main__:

return_asap(anything)
    あたえられた引数をそのまま返す
(END)
```
## 忘れた頃に見るところ
- python にポインタはない。たとえ `*args` という表記があっても、それはbashでいうところの `*` に近いというイメージがあればいいと思う。詳しくは関数定義の引数の項へ。