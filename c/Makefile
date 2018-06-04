CC=gcc

FILES=tree_node.c red_black_tree.c red_black_tree_test.c

OUT=bin/test_tree

build: $(FILES)
	$(CC) -o $(OUT) $(FILES)

clean:
	rm bin/*

rebuild:
	clean build
