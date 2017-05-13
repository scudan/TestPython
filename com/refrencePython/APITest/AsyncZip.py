import threading,zipfile


class AsyncZip(threading.Thread):
    def __init__(self,infile,outfile):
        threading.Thread .__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile,'w',zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print("finished backGround zip of:",self.infile)

bg = AsyncZip('myfile.txt','myarch.zip')
bg.start();
print("run in foreground")
bg.join()


bg1 = AsyncZip('myfile.txt','myarch.zip')
bg1.start();
bg1.join()

print("was done")