from flask import Flask
from flask_restful import Resource, Api
import MeCab

mecab = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

app = Flask(__name__)
api = Api(app)

class Morphologic(Resource):
    CONST_PARTS＿NOUN = "名詞"
    CONST_DEF_TARGET = "NiziUが好きな５０のWithU"

    def __init__(self):
        self.target = self.CONST_DEF_TARGET
        self.node_data = []
        
    def get(self, words):
        self.__words(words)
        self.__create_list(self.target)
        return self.node_data

    def __create_list(self, data):
        node = self.__node(data)
        while node:
            feature = self.__feature(node)
            if (self.__check(feature)):
                self.node_data.append(self.__set(node.surface, feature))
            node = node.next
        print(self.node_data)

    def __words(self, data):
        if (len(data) > 0):
            self.target = data

    def __node(self, data):
        mecab.parse("")
        return mecab.parseToNode(data)

    def __feature(self, data):
        return data.feature.split(",")

    def __check(self, data):
        return (data[0] == self.CONST_PARTS＿NOUN)

    def __set(self, surface, feature):
        data = {"surface": surface, "feature": feature}
        print(data)
        return data

api.add_resource(Morphologic, '/targetwords/<string:words>')

if __name__ == '__main__':
    app.run()


