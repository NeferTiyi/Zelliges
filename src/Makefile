ROOTDOC := "MemoireZelliges"

RM := rm -vf
LTXMK := latexmk -pdf
LTXCL := latexmk -f

# You want latexmk to *always* run, because make does not have all 
# the info. Also, include non-file targets in .PHONY so they are run 
# regardless of any file of the given name existing.
.PHONY: $(ROOTDOC).pdf all clean

# CUSTOM BUILD RULES

# In case you didn't know, '$@' is a variable holding the name of 
# the target, and '$<' is a variable holding the (first) dependancy 
# of a rule.

# HTXSRCS := $(shell ls *.htx)
# HTXOBJS := $(HTXSRCS:.htx=.tex)
TMPOBJS := $(ROOTDOC).bbl \
	   $(ROOTDOC).dic \
	   $(ROOTDOC).run.xml

# %.tex: %.htx
# 	htx2tex $<

# MAIN LATEXMK RULE

# -pdf tells latexmk to generate PDF directly (instead of DVI).
# -pdflatex="" tells latexmk to call a specific backend with specific
# options.
# -use-make tells latexmk to call make for generating missing files.

# -interactive=nonstopmode keeps the pdflatex backend from stopping 
# at a missing file reference and interactively asking you for an 
# alternative.

# $(ROOTDOC).pdf: $(HTXOBJS)
$(ROOTDOC).pdf:
	$(LTXMK) $(ROOTDOC).tex

# Cleaning
cleantmp:
	@$(RM) $(HTXOBJS) $(TMPOBJS)

cleanltxc:
	$(LTXCL) -c ($ROOTDOC).tex

cleanltxC:
	$(LTXCL) -C ($ROOTDOC).tex

clean: cleanltxc cleantmp

realclean: cleanltxC cleantmp
