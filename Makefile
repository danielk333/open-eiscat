build:
	python build_page.py docs/assets/software.csv docs/
	mkdocs build --site-dir public

serve:
	mkdocs serve