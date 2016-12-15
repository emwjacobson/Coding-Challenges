from chan import Chan

chan = Chan('b')
threads = chan.getThreads()
for thread in threads:
    posts = chan.getPosts(thread)
    images = chan.getImages(thread)
