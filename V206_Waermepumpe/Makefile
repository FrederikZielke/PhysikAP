all: build/V206.pdf

# hier Python-Skripte:
#build/plot.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
#	# so that matplotlib can find the tex header when running
#	# LaTeX in the tmp directory
#	# and set the matplotlibrc
#	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py

build/temperaturplots.pdf: temperaturplots.py | build
	python temperaturplots.py

build/ausgleichsplot.pdf: ausgleichsrechnung.py | build
	python ausgleichsrechnung.py

build/dampfdruck.pdf: auswertung.py | build
	python auswertung.py

# hier weitere Abhängigkeiten für build/V206.pdf deklarieren:
build/V206.pdf: build/temperaturplots.pdf build/ausgleichsplot.pdf build/dampfdruck.pdf

build/V206.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V206.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
