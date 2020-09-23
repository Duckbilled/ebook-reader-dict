"""Portuguese language."""

# Regex to find the pronunciation
pronunciation = r"{AFI\|\[([^\]]+)\]}"

# Regex to find the genre
genre = r"{([fm]+)}"

# Float number separator
float_separator = ","

# Thousads separator
thousands_separator = " "

# Markers for sections that contain interesting text to analyse.
section_patterns = (r"\#", r"\*")
section_level = 1
section_sublevels = (2,)
head_sections = ("{{-pt-}}",)
sections = (
    "Abreviatura",
    "Acrônimo",
    "Adjetivo",
    "Advérbio",
    "Antepositivo",
    "Artigo",
    "Contração",
    "Interjeição",
    "Numeral",
    "Prefixo",
    "Preposição",
    "Pronome",
    "Sigla",
    "Substantivo",
    "Sufixo",
    "Verbo",
)

# Some definitions are not good to keep (plural, genre, ... )
definitions_to_ignore = ("peçodef",)

# Templates to ignore: the text will be deleted.
templates_ignored = ("cont",)

# Templates that will be completed/replaced using italic style.
templates_italic = {
    "antigo": "arcaico",
    "Calão": "obsceno",
    "coloquialismo": "coloquial",
    "Coloquialismo": "coloquial",
    "Crustáceo": "Zoologia",
    "Figurado": "figurado",
    "Flor": "Botânica",
    "Informal": "coloquial",
    "Planta": "Botânica",
    "Popular": "coloquial",
    "réptil": "Zoologia",
}

# Templates more complex to manage.
templates_multi = {
    # {{escopo|Pecuária}}
    # {{escopo|pt|estrangeirismo}}
    # {{escopo|pt|coloquial|brasil}}
    "escopo": "term(lookup_italic(concat(parts, sep=' e ', indexes=[2, 3, 4, 5], skip='_'), 'pt') or parts[1])",
    # {{escopo2|Informática}}
    # {{escopo2|Brasil|governo}}
    "escopo2": "term(parts[1])",
    # {{escopoCat|Náutica|pt}}
    "escopoCat": "term(parts[1])",
    # {{escopoCatLang|Verbo auxiliar|pt}}
    "escopoCatLang": "term(parts[1])",
    # {{escopoUso|Portugal|pt}}
    "escopoUso": "term(lookup_italic(parts[1], 'pt'))",
    # {{fem|heliostático}}
    "fem": 'f"feminino de {strong(parts[1])}"',
    # {{l|pt|usar|usar}}",
    "l": "parts[-1]",
    # {{l.s.|uso}}
    "l.s.": "parts[-1]",
    # {{link preto|ciconiforme}}
    "link preto": "parts[-1]",
    # {{ll|publicar}}
    "ll": "parts[-1]",
    # {{mq|palavra}}
    # {{mq|word|en}}
    "mq": 'f"o mesmo que {strong(parts[1]) if len(parts) == 2 else italic(parts[1])}"',
    # {{varort|tenu-|pt}}
    "varort": 'f"variante ortográfica de {strong(parts[1])}"',
}

# Release content on GitHub
# https://github.com/BoboTiG/ebook-reader-dict/releases/tag/pt
release_description = """\
As palavras contam: {words_count}
Exportação Wikcionário: {dump_date}

:arrow_right: Descarregar: [dicthtml-{locale}.zip]({url})

---

Instalação:

1. Copiar o ficheiro `dicthtml-{locale}.zip` para a pasta `.kobo/dict/` do leitor.
2. Reiniciar o leitor.

---

Características:

- Não há etimologia.
- Os nomes próprios não estão incluídos.
- Os verbos conjugados não estão incluídos.

<sub>Actualizado em {creation_date}</sub>
"""

# Dictionary name that will be printed below each definition
wiktionary = "Wikcionário (ɔ) {year}"
