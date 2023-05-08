all: build/V500.pdf

# hier Python-Skripte:
#build/plot.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
#	# so that matplotlib can find the tex header when running
#	# LaTeX in the tmp directory
#	# and set the matplotlibrc
#	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py

build/plotLila.pdf: plotLila.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plotLila.py

build/plotGelb.pdf: plotGelb.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plotGelb.py

build/plotGruen.pdf: plotGruen.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plotGruen.py	

build/plotRot.pdf: plotRot.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plotRot.py

build/frequenz.pdf: frequenz.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python frequenz.py

# hier weitere Abhängigkeiten für build/V500.pdf deklarieren:
build/V500.pdf: build/plotLila.pdf build/plotGelb.pdf build/plotGruen.pdf build/plotRot.pdf build/frequenz.pdf

build/V500.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
V500.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
