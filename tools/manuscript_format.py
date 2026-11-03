"""Keep source anchors invisible on GitHub and convert them for Pandoc builds."""
import re


def pandoc_headings(text):
    return re.sub(r'^<a id="([^"]+)"></a>\n\n(#{1,6} [^\n]+)$',
                  lambda m: m.group(2) + ' {#' + m.group(1) + '}', text, flags=re.M)


def reader_title(title, titles):
    """Spell out classification cross-references without losing scope qualifiers."""
    return re.sub(r'\d{2}(?:[A-Z](?:xx|\d{2})|-(?:XX|\d{2}))',
                  lambda m: '“' + titles[m.group()] + '”', title)
