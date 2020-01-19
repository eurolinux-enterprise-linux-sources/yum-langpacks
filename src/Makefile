NAME = yum-langpacks
VERSION = $(shell python setup.py -V)

DIST = dist

SRC_FILES = COPYING ChangeLog Makefile README langpacks.conf langpacks.py setup.py yum-langpacks.8

$(NAME)-$(VERSION).tar.gz:
	mkdir -p dist
	mkdir dist/$(NAME)-$(VERSION)
	cp -p $(SRC_FILES) dist/$(NAME)-$(VERSION)
	tar zcvf $(NAME)-$(VERSION).tar.gz -C dist $(NAME)-$(VERSION)

clean:
	rm -rf *~ dist/*

upload:
	scp $(NAME)-$(VERSION).tar.gz fedorahosted.org:$(NAME)

git-tag:
	git tag $(VERSION)

git-push:
	git push
	git push --tags

