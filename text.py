import os


class Solution:
    def __init__(self):
        self.dirPath = []

    def numberOfCode(self, path):
        #找到所有.py的文件
        for dir in os.listdir(path):
            childDir = os.path.join(path, dir)
            if os.path.isdir(childDir):
                self.numberOfCode(childDir)
            else:
                if childDir[-2:] == "py":
                    self.dirPath.append(childDir)
        return self.dirPath

    def setCode(self):
        #将.py文件结尾的内容复制到text.txt
        with open("./text.txt", "ab+") as f:
            for file in self.dirPath:
                content = open(file, "rb").read()
                f.write(content)

    def clearCode(self):
        #将文件中的注释去掉，写入一个新的文件中
        with open("./text2.txt", "w+", encoding='utf-8') as f:
            a = open("./text.txt", 'r+', encoding='utf-8')
            line = a.readline()
            while line:
                if line.find('#') == -1 and line.find('"""') == -1:
                    f.write(line)
                elif line.find('"""'):
                    while True:
                        line = a.readline()
                        if line.find('"""'):
                            break
                line = a.readline()

    @staticmethod
    def split_code():
        #将text2中的文件每一万行分割成一个新的文件
        with open("./text2.txt", "r+", encoding='utf-8') as f:
            index = 1
            while True:
                with open("./" + str(index) + ".txt", 'w+', encoding='utf-8') as w:
                    for i in range(10000):
                        w.write(f.readline())
                index += 1
                if f.readline() == '':
                    break

    @staticmethod
    def _text(line):
        #翻转除了关键之之外的单词
        import keyword
        num = 0
        for index, item in enumerate(line[:-1]):
            if line[index].isalpha() and num == 0:
                length = 1
                while line[index + length].isalpha():
                    length += 1
                    if index + length == len(line):
                        break
                num = length
                word = line[index:index + length]
                if not keyword.iskeyword(word):
                    line = line[:index] + word[::-1] + line[index + length:]
            elif num != 0:
                num -= 1

        return line

    def confuse_code(self):
        #将反转之后的字符串写到新的文件中
        for index in range(1, 10):
            with open("./" + str(index) + ".txt", 'r+', encoding='utf-8') as r:
                with open("./new/" + str(index) + ".txt", 'w+', encoding='utf-8') as w:
                    while True:
                        line = r.readline()
                        w.write(self._text(line))
                        if r.readline() == '':
                            break


s = Solution()
# s.numberOfCode('./django')
# s.setCode()
# s.clearCode()
# s.split_code()
s.confuse_code()
