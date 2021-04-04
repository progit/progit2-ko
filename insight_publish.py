#-*- coding: utf-8 -*-
import re
import os

def parse_comment(line):
	global book, block, in_block

	if line.startswith('/////'):
		book.append("<원문>\n")
		book.extend(block)
		book.append("</원문>\n\n")

		block = []
		in_block = ''
	else:
	  block.append(line)


def parse(line):
	global book, depth, cwd, block, in_block

	# block - comment
	if in_block == 'comment':
		parse_comment(line)
		return

	# comment
	if line.startswith('/////'):
		in_block = 'comment'
		return

	# metadata
	if line.startswith(':'):
		return
	
	# include	
	m = re.match(r"include::(.*)\[\]", line)
	if m:
		path = cwd + "/" + m.group(1)
		old_cwd = cwd
		depth += 1
		with open(path) as f:
			cwd = os.path.dirname(path)
			for line in f.readlines():
				parse(line)
		depth -= 1
		cwd = old_cwd
		return

	# chapter
	m = re.match(r"== (.*)", line)
	if m:
		book.append("<장> " + m.group(1) + "\n")
		return

	# section
	m = re.match(r"=== (.*)", line)
	if m:
		book.append("<절> " + m.group(1) + "\n")
		return
	m = re.match(r"==== (.*)", line)
	if m:
		book.append("<소> " + m.group(1) + "\n")
		return
	m = re.match(r"===== (.*)", line)
	if m:
		book.append("<소소> " + m.group(1) + "\n")
		return

	# anchor
	m = re.match(r"^\[\[(.*)\]\]$", line)
	if m:
		book.append("<책갈피 이름=" + m.group(1) + ">\n")
		return

	# image
	if line.startswith('image::images/'):
		line = line.replace('image::images/', '<그림> ')

	# index
	line = re.sub(r"\(\(\((.*?)\)\)\)", r" <인덱스=\1>", line)

	# ref
	line = re.sub(r"<<(.*)>>", r"<책갈피 대상=\1>", line)

	book.append(line)

book = []
depth = 1
cwd = '.'
block = []
in_block = ''

asc_files = [
		'book/01-introduction/1-introduction.asc',
		'book/02-git-basics/1-git-basics.asc',
		'book/03-git-branching/1-git-branching.asc',
		'book/04-git-server/1-git-server.asc',
		'book/05-distributed-git/1-distributed-git.asc',
		'book/06-github/1-github.asc',
		'book/07-git-tools/1-git-tools.asc',
		'book/08-customizing-git/1-customizing-git.asc',
		'book/09-git-and-other-scms/1-git-and-other-scms.asc',
		'book/10-git-internals/1-git-internals.asc',
		'book/A-git-in-other-environments/1-git-other-environments.asc',
		'book/B-embedding-git/1-embedding-git.asc',
		'book/C-git-commands/1-git-commands.asc',
		'book/contributors.asc',
		'book/index.asc',
		'book/introduction.asc',
		'book/preface.asc',
		'book/toc.asc']

for asc_file in asc_files:
	book = []
	path = cwd + "/" + asc_file
	with open(path) as f:
		old_cwd = cwd
		for line in f.readlines():
			cwd = os.path.dirname(path)
			parse(line)
		cwd = old_cwd

	out_name = 'publish_' + asc_file.replace('/', '_') + '.txt'
	with open(out_name, 'w') as f:
		print len(book), out_name
		for line in book:
			f.write(line)