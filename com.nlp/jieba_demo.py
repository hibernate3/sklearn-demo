import jieba


if __name__ == '__main__':
    content = "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"

    # 试图将句子最精确地切开，适合文本分析
    result = jieba.lcut(content, cut_all=False)
    print(result)

    # 把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能消除 歧义
    result = jieba.lcut(content, cut_all=True)
    print(result)

    # 在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词
    result = jieba.lcut_for_search(content)
    print(result)
    pass

