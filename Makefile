all:
	@echo C218-MAKE-CANARY-EXECUTED
	gcc -o c218 main.c

clean:
	rm -f c218
