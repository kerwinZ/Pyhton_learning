import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud


class WordCloudClass:

    def __init__(self, filepath, background=None):
        self.filepath = filepath
        if background is None:
            self.mask = None
        else:
            self.mask = plt.imread(background)

    def get_text(self):
        """获取生成词云的文本内容"""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return content

    def text_process(self):
        """对文本内容进行分词处理"""
        text_list = jieba.lcut(self.get_text())
        text = ' '.join(text_list)
        return text

    def generate_pic(self):
        """生成词云图片"""
        # 中文字体需要更换
        wc = WordCloud(font_path='/System/Library/Fonts/STHeiti Light.ttc',
                       background_color='white',
                       mask=self.mask
                       )
        my_wordCloud = wc.generate(self.text_process())
        plt.imshow(my_wordCloud)
        plt.axis('off')
        plt.show()
        my_wordCloud.to_file("wordCloud.png")


if __name__ == '__main__':
    path = 'wordCloud.txt'
    background_path = 'pic.jpeg'

    # a = WordCloudClass(path)
    a = WordCloudClass(path, background_path)
    a.generate_pic()
