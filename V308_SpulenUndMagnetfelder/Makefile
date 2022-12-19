all: build/V308.pdf

# hier Python-Skripte:
#build/plot.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
#	# so that matplotlib can find the tex header when running
#	# LaTeX in the tmp directory
#	# and set the matplotlibrc
#	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py

#build/helmholtz.pdf: helmholtz.py ../matplotlibrc ../header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python helmholtz.py
#
#build/hysterese.pdf: hysterese.py ../matplotlibrc ../header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python hysterese.py
#
#build/spulen.pdf: spulen.py ../matplotlibrc ../header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python spulen.py

# hier weitere Abhängigkeiten für build/V000.pdf deklarieren:
#build/V308.pdf: build/hysterese.pdf build/helmholtz.pdf build/spulen.pdf

build/V308.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V308.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
