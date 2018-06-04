CC=gcc

FLAGS=-Wall

FILES=tree_node.c red_black_tree.c red_black_tree_test.c

OUT=bin/test_tree

build: $(FILES)
	$(CC) -o $(OUT) $(FILES) $(FLAGS)

clean:
	rm bin/*

rebuild:
	clean build
