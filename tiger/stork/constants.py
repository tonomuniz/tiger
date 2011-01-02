FONT_ARIAL = 'Frutiger, "Frutiger Linotype", Univers, Calibri, "Gill Sans", "Gill Sans MT", "Myriad Pro", Myriad, "DejaVu Sans Condensed", "Liberation Sans", "Nimbus Sans L", Tahoma, Geneva, "Helvetica Neue", Helvetica, Arial, sans-serif'
FONT_GARAMOND = '"Palatino Linotype", Palatino, Palladio, "URW Palladio L", "Book Antiqua", Baskerville, "Bookman Old Style", "Bitstream Charter", "Nimbus Roman No9 L", Garamond, "Apple Garamond", "ITC Garamond Narrow", "New Century Schoolbook", "Century Schoolbook", "Century Schoolbook L", Georgia, serif'
FONT_GEORGIA = 'Constantia, "Lucida Bright", Lucidabright, "Lucida Serif", Lucida, "DejaVu Serif", "Bitstream Vera Serif", "Liberation Serif", Georgia, serif'
FONT_IMPACT = 'Impact, Haettenschweiler, "Franklin Gothic Bold", Charcoal, "Helvetica Inserat", "Bitstream Vera Sans Bold", "Arial Black", sans-serif'
FONT_MONOSPACE = 'Consolas, "Andale Mono WT", "Andale Mono", "Lucida Console", "Lucida Sans Typewriter", "DejaVu Sans Mono", "Bitstream Vera Sans Mono", "Liberation Mono", "Nimbus Mono L", Monaco, "Courier New", Courier, monospace'
FONT_TIMES = 'Cambria, "Hoefler Text", Utopia, "Liberation Serif", "Nimbus Roman No9 L Regular", Times, "Times New Roman", serif'
FONT_TREBUCHET = '"Segoe UI", Candara, "Bitstream Vera Sans", "DejaVu Sans", "Bitstream Vera Sans", "Trebuchet MS", Verdana, "Verdana Ref", sans-serif'
FONT_VERDANA = 'Corbel, "Lucida Grande", "Lucida Sans Unicode", "Lucida Sans", "DejaVu Sans", "Bitstream Vera Sans", "Liberation Sans", Verdana, "Verdana Ref", sans-serif'

FONT_CHOICES = (
    (FONT_ARIAL, 'Arial'),
    (FONT_GARAMOND, 'Garamond'),
    (FONT_GEORGIA, 'Georgia'),
    (FONT_IMPACT, 'Impact'),
    (FONT_MONOSPACE, 'Monospace'),
    (FONT_TIMES, 'Times New Roman'),
    (FONT_TREBUCHET, 'Trebuchet'),
    (FONT_VERDANA, 'Verdana'),
)


TEMPLATE_TAG_ESCAPES = (
    ('{%', '&#123;&#37;'),
    ('%}', '&#37;&#125;'),
    ('{{', '&#123;&#123;'),
    ('}}', '&#125;&#125;'),
    ('{#', '&#123;&#35;'),
    ('#}', '&#35;&#125;'),
)