all: build/V703.pdf

# hier Python-Skripte:
#build/kennlinie.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py
#
#build/strom.pdf: plot2.py ../matplotlibrc ../header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot2.py
#hier weitere Abhängigkeiten für build/V000.pdf deklarieren:
build/V703.pdf: build/strom.pdf build/kennlinie.pdf



build/V703.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V703.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
