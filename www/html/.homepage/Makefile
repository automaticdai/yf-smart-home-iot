.IGNORE:
SHELL = /bin/bash

SOURCES = index.txt research.txt publication.txt contact.txt cv.txt   wiki.txt blogs.txt projs.txt about.txt   wiki_linux.txt wiki_matlab.txt wiki_mysql.txt wiki_raspi.txt wiki_python.txt      blog_hard_soft_real_time.txt blog_classic_control.txt   proj_weather_report.txt

pagefiles=$(SOURCES:.txt=.html)

default: all giveaccess

all: $(pagefiles)

footbar.pm: footbar
	./Markdown.pl footbar > footbar.pm

sidebar.pm: sidebar
	./Markdown.pl sidebar > sidebar.pm

%.s: %.txt
	cat $*.txt globalauthor globalkeywords globaldescription  > $*.txt2
	./find_code.pl < $*.txt2 > $*.s

%.w: %.s
	./Markdown.pl $*.s > $*.w

%.html : %.w template footbar.pm sidebar.pm globalkeywords globalauthor globaldescription
	./preppage.pl template sidebar.pm footbar.pm $*.w | ./inc_file.pl > $*.html
	grep 'table_of_contents' $*.html && python ./pyhat.py -d. $*.html || echo $*.html generated

	
clean:
	/bin/rm -f $(pagefiles)
	
giveaccess:
	chmod -R a+r *

