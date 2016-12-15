import requests as r
import re

class Chan:

    baseUrl = "http://boards.4chan.org"

    def __init__(self, board):
        self.board = board

    def setBoard(self, board):
        self.board = board

    def getThreads(self):
        all_threads = []
        for pageNumber in range(1,11):
            if pageNumber == 1: pageNumber = ""
            url = "{}/{}/{}".format(self.baseUrl,self.board,pageNumber)
            response = r.get(url)
            threads = re.findall("\[<a href=\"thread\/(.*?)\/.*?\" class=\"replylink\">Reply<\/a>\]", response.text)
            all_threads = all_threads + threads
        return all_threads

    def setThread(self, thread):
        self.thread = thread

    def getPosts(self, thread):
        rtn = []
        url = "{}/{}/thread/{}".format(self.baseUrl, self.board,thread)
        response = r.get(url)
        posts = re.findall("<blockquote class=\"postMessage\" id=\"(.*?)\">(.*?)<\/blockquote>", response.text)
        for postid,text in posts:
            rtn.append((postid[1:],text))
        return rtn

    def getImages(self, thread):
        url = "{}/{}/thread/{}".format(self.baseUrl, self.board,thread)
        response = r.get(url)
        images = re.findall("File: <a href=\"\/\/(.*?)\" target=\"_blank\">(.*?)<\/a>", response.text)
        return images
