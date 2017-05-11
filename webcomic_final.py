import urllib, re, zipfile
script_dir = "/home"


def write_zip(filename, ifile):
    
    rel_path = "/COMIC-SMBC/SMBC.cbz"
    abs_file_path = script_dir+rel_path
    z = zipfile.ZipFile(abs_file_path,'a')
	
    if not filename in z.namelist():
        print "Converting", filename
        z.writestr(filename,ifile.read())
    z.close()

def geturl(text):
    for line in text:
        match = re.search(r'cc-comic',line)
        if match:
	    
            match = re.search(r'" src="(.*?)"',line)
            if match:
                url = match.group(1)
                return url        

def wget2(url, i):
    rel_file = "/COMIC-SMBC/file" + str(i) + ".jpeg"
    filename = script_dir + rel_file
    
    try:
        ufile = urllib.urlopen(url)
        text = ufile.readlines()
        url = geturl(text)
        try:
		
        	imgfile = urllib.urlopen(str(url))
        	write_zip(filename,imgfile)
            
        except:
            print filename, "not converted"
            return
           
    except IOError:
        print 'problem reading url: +', url
	

def getpage(url):
    ufile = urllib.urlopen(url)
    text = ufile.readlines()
    url = geturl(text)
    for line in text:
        match = re.search(r'class="prev"',line)
        if match:
		
        	match = re.search(r'"start"></a><a href="(.*?)"',line)
        	if match:
                	url = match.group(1)
               		return url

def main():
    url = "http://www.smbc-comics.com/"
    i=1;
    while True:
        wget2(url, i)
	if (url=="http://www.smbc-comics.com/comic/2002-09-05"	):
		break
	url=getpage(url)
	i+=1
    print "DONE"

if __name__ == '__main__':
  main()
