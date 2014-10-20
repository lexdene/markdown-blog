STYLE_COMPILER = sass
SCRIPT_COMPILER = coffee -b -c -o
MIN_SCRIPT_COMPILER = uglifyjs -o
MKDIR = mkdir -p

# dir
SOURCE_DIR = .
TARGET_DIR = ../data/compiled

# dir for sass
STYLE_SOURCE_DIR = $(SOURCE_DIR)/sass
STYLE_TARGET_DIR = $(TARGET_DIR)/css

# dir for coffee script
SCRIPT_SOURCE_DIR = $(SOURCE_DIR)/coffee
SCRIPT_TARGET_DIR = $(TARGET_DIR)/js

# sass file list
STYLE_SOURCES = $(shell find $(STYLE_SOURCE_DIR) -name '*.sass')
STYLE_TARGETS = $(patsubst $(STYLE_SOURCE_DIR)/%.sass, $(STYLE_TARGET_DIR)/%.css, $(STYLE_SOURCES))

# coffee script file list
SCRIPT_SOURCES = $(shell find $(SCRIPT_SOURCE_DIR) -name '*.coffee')
SCRIPT_TARGETS = $(patsubst $(SCRIPT_SOURCE_DIR)/%.coffee, $(SCRIPT_TARGET_DIR)/%.js, $(SCRIPT_SOURCES))
SCRIPT_COMPRESSED_TARGETS = $(patsubst $(SCRIPT_TARGET_DIR)/%.js, $(SCRIPT_TARGET_DIR)/%.min.js, $(SCRIPT_TARGETS))

TARGETS = $(STYLE_TARGETS) $(SCRIPT_TARGETS) $(SCRIPT_COMPRESSED_TARGETS)

first : all

# compile for files
$(STYLE_TARGET_DIR)/%.css : $(STYLE_SOURCE_DIR)/%.sass Makefile
	$(STYLE_COMPILER) "$<" "$@"

$(SCRIPT_TARGET_DIR)/%.js : $(SCRIPT_SOURCE_DIR)/%.coffee Makefile
	$(SCRIPT_COMPILER) $$(dirname "$@") "$<"

$(SCRIPT_TARGET_DIR)/%.min.js : $(SCRIPT_TARGET_DIR)/%.js
	$(MIN_SCRIPT_COMPILER) "$@" "$<"

# auto make dir
define depend_on_dir
$(1): | $(dir $(1))
ifndef $(dir $(1))_DIRECTORY_RULE_IS_DEFINED
$(dir $(1)):
	$(MKDIR) $$@

$(dir $(1))_DIRECTORY_RULE_IS_DEFINED := 1
endif
endef

$(foreach file, $(TARGETS), $(eval $(call depend_on_dir, $(file))))

# all
all: $(TARGETS)

clean:
	rm -rv $(TARGET_DIR)
