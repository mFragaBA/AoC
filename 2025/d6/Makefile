SHELL := /bin/bash

%: %.odin
	odin run $< -file -out:$@.bin

clean:
	rm -f *.bin
