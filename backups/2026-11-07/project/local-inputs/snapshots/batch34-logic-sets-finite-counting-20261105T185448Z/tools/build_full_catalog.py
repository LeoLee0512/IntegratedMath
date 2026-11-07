#!/usr/bin/env python3
"""Build the complete MSC-based writing catalog; index entries are not completed prose.

Uses the user-provided PDF or its integrity-checked title cache to recover headings.
No original PDF, cross-reference prose, or chapter prose is redistributed here.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PDF = ROOT / 'local-inputs/MSC_2020.pdf'
HEADING = re.compile(r'^\s*(\d{2}-XX|\d{2}[A-Z]xx|\d{2}[A-Z]\d{2}|\d{2}-\d{2})\s+(.+)$')
OUTPUT_HEADING = re.compile(r'^(#{1,3}) 第(\d+)(部分|章|节) (.+)（(?:MSC )?([0-9A-Zx-]+)）$')
# These are lexical hyphens actually split at line endings in the supplied PDF.
# Other end-of-line hyphens in its headings are typographical word breaks.
KEEP_WRAPPED_HYPHEN = {'infinite', 'information', 'time', 'initial', 'non'}
EXPECTED = {'major': 63, 'intermediate': 534, 'subject_leaf': 5503, 'general_leaf': 503}

# Per-code mathematical headings verified from the uploaded PDF, not inferred from topic names.
MATH_TITLE_OVERRIDES = {'05A30': '$q$-calculus and related topics',
 '11B50': 'Sequences (mod $m$)',
 '11B57': 'Farey sequences; the sequences $1^k,2^k,\\ldots$',
 '11B65': 'Binomial coefficients; factorials; $q$-identities',
 '11D88': '$p$-adic and power series fields',
 '11E70': '$K$-theory of quadratic and Hermitian forms',
 '11E95': '$p$-adic theory',
 '11F33': 'Congruences for modular and $p$-adic modular forms',
 '11F66': 'Langlands $L$-functions; one variable Dirichlet series and functional equations',
 '11F67': 'Special values of automorphic $L$-series, periods of automorphic forms, cohomology, modular symbols',
 '11F85': '$p$-adic theory, local fields',
 '11G10': 'Abelian varieties of dimension $>1$',
 '11G30': 'Curves of arbitrary genus or genus $\\ne 1$ over global fields',
 '11G40': '$L$-functions of varieties over global fields; Birch-Swinnerton-Dyer conjecture',
 '11G55': 'Polylogarithms and relations with $K$-theory',
 '11J93': 'Transcendence theory of Drinfel’d and $t$-modules',
 '11K41': 'Continuous, $p$-adic and abstract analogues',
 '11M06': '$\\zeta(s)$ and $L(s,\\chi)$',
 '11M20': 'Real zeros of $L(s,\\chi)$; results on $L(1,\\chi)$',
 '11M26': 'Nonreal zeros of $\\zeta(s)$ and $L(s,\\chi)$; Riemann and other hypotheses',
 '11M38': 'Zeta and $L$-functions in characteristic $p$',
 '11Mxx': 'Zeta and $L$-functions: analytic theory',
 '11R42': 'Zeta functions and $L$-functions of number fields',
 '11R54': 'Other algebras and orders, and their zeta and $L$-functions',
 '11R59': 'Zeta functions and $L$-functions of function fields',
 '11R70': '$K$-theory of global fields',
 '11S31': 'Class field theory; $p$-adic formal groups',
 '11S40': 'Zeta functions and $L$-functions',
 '11S70': '$K$-theory of local fields',
 '11S80': 'Other analytic theory (analogues of beta and gamma functions, $p$-adic integration, etc.)',
 '12H25': '$p$-adic differential equations',
 '12J12': 'Formally $p$-adic fields',
 '13A35': 'Characteristic $p$ methods (Frobenius endomorphism) and reduction to characteristic $p$; tight closure',
 '13D15': 'Grothendieck groups, $K$-theory and commutative rings',
 '14C35': 'Applications of methods of algebraic $K$-theory in algebraic geometry',
 '14F30': '$p$-adic cohomology, crystalline cohomology',
 '14J28': '$K3$ surfaces and Enriques surfaces',
 '14J40': '$n$-folds ($n>4$)',
 '14L05': 'Formal groups, $p$-divisible groups',
 '16E20': 'Grothendieck groups, $K$-theory, etc.',
 '16R10': '$T$ -ideals, identities, varieties of associative rings and algebras',
 '16Y80': '$\\Gamma$ and fuzzy structures',
 '17A42': 'Other $n$-ary compositions ($n\\ge 3$)',
 '17D20': '$(\\gamma,\\delta)$-rings, including $(1,-1)$-rings',
 '18F25': 'Algebraic $K$-theory and $L$-theory (category-theoretic aspects)',
 '18G70': '$A_{\\infty}$-categories, relations with homological mirror symmetry',
 '18N20': 'Tricategories, weak $n$-categories, coherence, semi-strictification',
 '18N45': 'Categories of fibrations, relations to $K$-theory, relations to type theory',
 '18N60': '$(\\infty,1)$-categories (quasi-categories, Segal spaces, etc.); $\\infty$-topoi, stable '
          '$\\infty$-categories',
 '18N65': '$(\\infty,n)$-categories and $(\\infty,\\infty)$-categories',
 '18N70': '$\\infty$-operads and higher algebra',
 '19-00': 'General reference works (handbooks, dictionaries, bibliographies, etc.) pertaining to $K$-theory',
 '19-01': 'Introductory exposition (textbooks, tutorial papers, etc.) pertaining to $K$-theory',
 '19-02': 'Research exposition (monographs, survey articles) pertaining to $K$-theory',
 '19-03': 'History of $K$-theory',
 '19-04': 'Software, source code, etc. for problems pertaining to $K$-theory',
 '19-06': 'Proceedings, conferences, collections, etc. pertaining to $K$-theory',
 '19-08': 'Computational methods for problems pertaining to $K$-theory',
 '19-11': 'Research data for problems pertaining to $K$-theory',
 '19-XX': '$K$-theory',
 '19A31': '$K_0$ of group rings and orders',
 '19A49': '$K_0$ of other rings',
 '19Axx': 'Grothendieck groups and $K_0$',
 '19B28': '$K_1$ of group rings and orders',
 '19Bxx': 'Whitehead groups and $K_1$',
 '19C20': 'Symbols, presentations and stability of $K_2$',
 '19C30': '$K_2$ and the Brauer group',
 '19C40': 'Excision for $K_2$',
 '19Cxx': 'Steinberg groups and $K_2$',
 '19D06': '$Q$- and plus-constructions',
 '19D10': 'Algebraic $K$-theory of spaces',
 '19D25': 'Karoubi-Villamayor-Gersten $K$-theory',
 '19D35': 'Negative $K$-theory, NK and Nil',
 '19D45': 'Higher symbols, Milnor $K$-theory',
 '19D50': 'Computations of higher $K$-theory of rings',
 '19D55': '$K$-theory and homology; cyclic homology and cohomology',
 '19Dxx': 'Higher algebraic $K$-theory',
 '19E08': '$K$-theory of schemes',
 '19E15': 'Algebraic cycles and motivic cohomology ($K$-theoretic aspects)',
 '19E20': 'Relations of $K$-theory with cohomology theories',
 '19Exx': '$K$-theory in geometry',
 '19F05': 'Generalized class field theory ($K$-theoretic aspects)',
 '19F15': 'Symbols and arithmetic ($K$-theoretic aspects)',
 '19F27': 'Étale cohomology, higher regulators, zeta and $L$-functions ($K$-theoretic aspects)',
 '19Fxx': '$K$-theory in number theory',
 '19G24': '$L$-theory of group rings',
 '19G38': 'Hermitian $K$-theory, relations with $K$-theory of rings',
 '19Gxx': '$K$-theory of forms',
 '19J05': 'Finiteness and other obstructions in $K_0$',
 '19J25': 'Surgery obstructions ($K$-theoretic aspects)',
 '19J35': 'Obstructions to group actions ($K$-theoretic aspects)',
 '19K14': '$K_0$ as an ordered group, traces',
 '19K33': 'Ext and $K$-homology',
 '19K35': 'Kasparov theory ($KK$-theory)',
 '19Kxx': '$K$-theory and operator algebras',
 '19L20': '$J$-homomorphism, Adams operations',
 '19L41': 'Connective $K$-theory, cobordism',
 '19L47': 'Equivariant $K$-theory',
 '19L50': 'Twisted $K$-theory; differential $K$-theory',
 '19L64': 'Geometric applications of topological $K$-theory',
 '19Lxx': 'Topological $K$-theory',
 '19M05': 'Miscellaneous applications of $K$-theory',
 '19Mxx': 'Miscellaneous applications of $K$-theory',
 '20C11': '$p$-adic representations of finite groups',
 '20D10': 'Finite solvable groups, theory of formations, Schunck classes, Fitting classes, $\\pi$-length, ranks',
 '20D15': 'Finite nilpotent groups, $p$-groups',
 '20D20': 'Sylow subgroups, Sylow properties, $\\pi$-groups, $\\pi$-structure',
 '20E42': 'Groups with a $BN$ -pair; buildings',
 '20G43': 'Schur and $q$-Schur algebras',
 '20N15': '$n$-ary systems ($n\\ge 3$)',
 '22D25': '$C^{*}$-algebras and $W^{*}$-algebras in relation to group representations',
 '22E35': 'Analysis on $p$-adic Lie groups',
 '26E10': '$C^{\\infty}$-functions, quasi-analytic functions',
 '28A05': 'Classes of sets (Borel fields, $\\sigma$-rings, etc.), measurable sets, Suslin sets, analytic sets',
 '30C65': 'Quasiconformal mappings in $\\mathbb{R}^{n}$, other generalizations',
 '30G20': 'Generalizations of Bers and Vekua type (pseudoanalytic, $p$-analytic, etc.)',
 '30H25': 'Besov spaces and $Q_p$-spaces',
 '32A35': '$H^p$-spaces, Nevanlinna spaces of functions in several complex variables',
 '32C38': 'Sheaves of differential operators and their modules, $D$-modules',
 '32F10': '$q$-convexity, $q$-concavity',
 '32J18': 'Compact complex $n$-folds',
 '32M17': 'Automorphism groups of $\\mathbb{C}^{n}$ and affine manifolds',
 '32M25': 'Complex vector fields, holomorphic foliations, $\\mathbb{C}$-actions',
 '32Q02': 'Special domains (Reinhardt, Hartogs, circular, tube, etc.) in $\\mathbb{C}^{n}$ and complex manifolds',
 '32S40': 'Monodromy; relations with differential equations and $D$-modules (complex-analytic aspects)',
 '32W05': '$\\bar{\\partial}$ and $\\bar{\\partial}$-Neumann operators',
 '32W10': '$\\bar{\\partial}_b$ and $\\bar{\\partial}_b$-Neumann operators',
 '33C05': 'Classical hypergeometric functions, ${}_2F_1$',
 '33C10': 'Bessel and Airy functions, cylinder functions, ${}_0F_1$',
 '33C15': 'Confluent hypergeometric functions, Whittaker functions, ${}_1F_1$',
 '33C20': 'Generalized hypergeometric series, ${}_pF_q$',
 '33C60': 'Hypergeometric integrals and functions defined by them ($E$, $G$, $H$ and $I$ functions)',
 '33D05': '$q$-gamma functions, $q$-beta functions and integrals',
 '33D15': 'Basic hypergeometric functions in one variable, ${}_r\\phi_s$',
 '33D80': 'Connections of basic hypergeometric functions with quantum groups, Chevalley groups, $p$-adic groups, Hecke '
          'algebras, and related topics',
 '33E50': 'Special functions in characteristic $p$ (gamma functions, etc.)',
 '35J92': 'Quasilinear elliptic equations with $p$-Laplacian',
 '35K92': 'Quasilinear parabolic equations with $p$-Laplacian',
 '35N15': '$\\bar{\\partial}$-Neumann problems and formal complexes in context of PDEs',
 '37A55': 'Dynamical systems and the theory of $C^{*}$-algebras',
 '37C85': 'Dynamics induced by group actions other than $\\mathbb{Z}$ and $\\mathbb{R}$, and $\\mathbb{C}$',
 '39A13': 'Difference equations, scaling ($q$-differences)',
 '42B30': '$H^p$-spaces',
 '43A15': '$L^p$-spaces and other function spaces on groups, semigroups, etc.',
 '43A17': 'Analysis on ordered groups, $H^p$-theory',
 '43A20': '$L^1$-algebras on groups, semigroups, etc.',
 '46A19': 'Other “topological” linear spaces (convergence spaces, ranked spaces, spaces with a metric taking values in '
          'an ordered structure more general than $\\mathbb{R}$, etc.)',
 '46A30': 'Open mapping and closed graph theorems; completeness (including $B$-, $B_r$-completeness)',
 '46E30': 'Spaces of measurable functions ($L^p$-spaces, Orlicz spaces, Köthe function spaces, Lorentz spaces, '
          'rearrangement invariant spaces, ideal spaces, etc.)',
 '46J15': 'Banach algebras of differentiable or analytic functions, $H^p$-spaces',
 '46L05': 'General theory of $C^{*}$-algebras',
 '46L06': 'Tensor products of $C^{*}$-algebras',
 '46L08': '$C^{*}$-modules',
 '46L09': 'Free products of $C^{*}$-algebras',
 '46L35': 'Classifications of $C^{*}$-algebras',
 '46L45': 'Decomposition theory for $C^{*}$-algebras',
 '46L57': 'Derivations, dissipations and positive semigroups in $C^{*}$-algebras',
 '46L80': '$K$-theory and operator algebras (including cyclic theory)',
 '46L89': 'Other “noncommutative” mathematics based on $C^{*}$-algebra theory',
 '46Lxx': 'Selfadjoint operator algebras ($C^{*}$-algebras, von Neumann ($W^{*}$-) algebras, etc.)',
 '46S10': 'Functional analysis over fields other than $\\mathbb{R}$ or $\\mathbb{C}$ or the quaternions; '
          'non-Archimedean functional analysis',
 '47B06': 'Riesz operators; eigenvalue distributions; approximation numbers, $s$-numbers, Kolmogorov numbers, entropy '
          'numbers, etc. of operators',
 '47B10': 'Linear operators belonging to operator ideals (nuclear, $p$-summing, in the Schatten-von Neumann classes, '
          'etc.)',
 '47C10': 'Linear operators in ${}^{*}$-algebras',
 '47C15': 'Linear operators in $C^{*}$- or von Neumann algebras',
 '47D60': '$C$-semigroups, regularized semigroups',
 '47H08': 'Measures of noncompactness and condensing mappings, $K$-set contractions, etc.',
 '47H09': 'Contraction-type mappings, nonexpansive mappings, $A$-proper mappings, etc.',
 '47L40': 'Limit algebras, subalgebras of $C^{*}$-algebras',
 '47S10': 'Operator theory over fields other than $\\mathbb{R}$, $\\mathbb{C}$ or the quaternions; non-Archimedean '
          'operator theory',
 '51E21': 'Blocking sets, ovals, $k$-arcs',
 '51L15': '$n$-vertex theorems via direct methods',
 '52A20': 'Convex sets in $n$ dimensions (including convex hypersurfaces)',
 '52B11': '$n$-dimensional polytopes',
 '52C07': 'Lattices and convex bodies in $n$ dimensions (aspects of discrete geometry)',
 '52C17': 'Packing and covering in $n$ dimensions (aspects of discrete geometry)',
 '52C22': 'Tilings in $n$ dimensions (aspects of discrete geometry)',
 '53A07': 'Higher-dimensional and -codimensional surfaces in Euclidean and related $n$-spaces',
 '53C10': '$G$-structures',
 '53C27': 'Spin and $\\operatorname{Spin}^{c}$ geometry',
 '53C70': 'Direct methods ($G$-spaces of Busemann, etc.)',
 '54C45': '$C$- and $C^{*}$-embedding',
 '54D10': 'Lower separation axioms ($T_0$–$T_3$, etc.)',
 '54D25': '“$P$ -minimal” and “$P$ -closed” spaces',
 '54D45': 'Local compactness, $\\sigma$-compactness',
 '54D50': '$k$-spaces',
 '54E18': '$p$-spaces, $M$-spaces, $\\sigma$-spaces, etc.',
 '54F50': 'Topological spaces of dimension $\\le 1$; curves, dendrites',
 '54G05': 'Extremally disconnected spaces, $F$ -spaces, etc.',
 '54G10': '$P$ -spaces',
 '55N15': 'Topological $K$-theory',
 '55P43': 'Spectra with additional structure ($E_{\\infty}$, $A_{\\infty}$, ring spectra, etc.)',
 '55P45': '$H$-spaces and duals',
 '55Q50': '$J$-morphism',
 '55Q51': '$v_n$-periodicity',
 '55R35': 'Classifying spaces of groups and $H$-spaces in algebraic topology',
 '55R45': 'Homology and homotopy of $B\\mathrm{O}$ and $B\\mathrm{U}$; Bott periodicity',
 '55R50': 'Stable classes of vector space bundles in algebraic topology and relations to $K$-theory',
 '55S25': '$K$-theory operations and generalized cohomology operations in algebraic topology',
 '55S45': 'Postnikov systems, $k$-invariants',
 '57N50': '$S^{n-1}\\subset E^n$, Schoenflies problem',
 '57R27': 'Controllability of vector fields on $C^{\\infty}$ and real-analytic manifolds',
 '57R80': '$h$- and $s$-cobordism',
 '57T25': 'Homology and cohomology of $H$-spaces',
 '60F25': '$L^p$-limit theorems',
 '60G65': 'Nonlinear processes (e.g., $G$-Brownian motion, $G$-Lévy processes)',
 '70F10': '$n$-body problems',
 '76F60': '$k$-$\\varepsilon$ modeling in turbulence',
 '81R10': 'Infinite-dimensional groups and algebras motivated by physics, including Virasoro, Kac-Moody, $W$ -algebras '
          'and other current algebras and their representations',
 '81U10': '$n$-body potential quantum scattering theory',
 '81U20': '$S$-matrix theory, etc. in quantum theory',
 '83C30': 'Asymptotic procedures (radiation, news functions, $\\mathcal{H}$-spaces, etc.) in general relativity and '
          'gravitational theory',
 '91A06': '$n$-person games, $n>2$',
 '93B36': '$H^{\\infty}$-control',
 '93D05': 'Lyapunov and other classical stabilities (Lagrange, Poisson, $L^p$, $l^p$, etc.) in control theory'}
VISUALLY_REVIEWED_MATH_CODES = ['11B57', '11G10', '11G30', '11M06', '11M20', '11M26', '14J28', '14J40', '16Y80', '17A42', '17D20', '18G70', '18N60', '18N65', '18N70', '19A31', '19A49', '19Axx', '19B28', '19Bxx', '19C20', '19C30', '19C40', '19Cxx', '19J05', '19K14', '20D10', '20D20', '20N15', '22D25', '26E10', '28A05', '30C65', '30H25', '32A35', '32M17', '32M25', '32Q02', '32W05', '32W10', '33C05', '33C10', '33C15', '33C20', '33D15', '35N15', '37A55', '37C85', '42B30', '43A15', '43A17', '43A20', '46A19', '46A30', '46E30', '46J15', '46L05', '46L06', '46L08', '46L09', '46L35', '46L45', '46L57', '46L89', '46Lxx', '46S10', '47C10', '47C15', '47L40', '47S10', '53C27', '54C45', '54D10', '54D45', '54E18', '54F50', '55P43', '55Q51', '55R45', '57N50', '57R27', '60F25', '76F60', '83C30', '91A06', '93B36', '93D05']
NAME_NORMALIZATIONS = {'11G32': {'after': 'Belyĭ',
           'before': 'Belyı̆',
           'reason': 'Unicode spelling normalization of a printed breve over dotless i; no translation.'}}
for name_code in ('41A17', '46B22', '46C20', '47H30'):
    NAME_NORMALIZATIONS[name_code] = {
        'before': 'ı̆', 'after': 'ĭ',
        'reason': 'Compose the printed breve-over-dotless-i spelling into its Unicode display form; no name translation.'}


MATH_TITLE_OVERRIDES['46A63'] = r'Topological invariants ($(\mathrm{DN})$, $(\Omega)$, etc.) for locally convex spaces'
VISUALLY_REVIEWED_MATH_CODES.append('46A63')


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def code_hash(codes) -> str:
    return sha256(('\n'.join(sorted(codes)) + '\n').encode('utf-8')).hexdigest()


def join_title(lines: list[str]) -> str:
    text = lines[0]
    for line in lines[1:]:
        match = re.search(r'([A-Za-z]+)-$', text)
        if match and re.match(r'[a-z]', line):
            if match.group(1) in KEEP_WRAPPED_HYPHEN:
                text += line
            else:
                text = text[:-1] + line
        else:
            text += ' ' + line
    # The headings' bracketed/braced portions are routing cross-references.
    text = re.split(r'\s*[\[{]', text, maxsplit=1)[0]
    return unicodedata.normalize('NFC', re.sub(r'\s+', ' ', text).strip())


def read_pdf_headings(pdf: Path) -> tuple[dict[str, str], dict[str, int]]:
    text = subprocess.run(['pdftotext', '-layout', str(pdf), '-'], capture_output=True,
                          text=True, check=True).stdout
    fragments: dict[str, list[str]] = {}
    pages: dict[str, int] = {}
    current = None
    for page_number, page in enumerate(text.split('\f'), 1):
        for line in page.splitlines():
            match = HEADING.match(line)
            if match:
                code, title = match.groups()
                if code in fragments:
                    raise ValueError(f'Duplicate PDF heading: {code}')
                current = code
                fragments[code] = [title.strip()]
                pages[code] = page_number
            elif current and line.strip() and not line.strip().isdigit():
                fragments[current].append(line.strip())
    return {code: join_title(lines) for code, lines in fragments.items()}, pages


def verify_catalog(path: Path, records: list[dict]) -> dict:
    """Parse the emitted Markdown independently of the rendering loop."""
    source = {row['code']: row for row in records}
    seen = []
    counters = Counter()
    major = chapter = None
    for line_number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.startswith('#'):
            continue
        match = OUTPUT_HEADING.fullmatch(line)
        if not match:
            raise ValueError(f'Unexpected catalog heading at line {line_number}: {line}')
        marks, number, unit, _title, code = match.groups()
        if code not in source:
            raise ValueError(f'Invented classification code: {code}')
        row = source[code]
        level = row['level']
        expected_unit = '部分' if level == 'major' else '章' if level == 'intermediate' else '节'
        expected_marks = '#' if level == 'major' else '##' if level == 'intermediate' else '###'
        if unit != expected_unit or marks != expected_marks:
            raise ValueError(f'Wrong hierarchy for {code}')
        counters[unit] += 1
        if int(number) != counters[unit]:
            raise ValueError(f'Non-contiguous {unit} numbering for {code}')
        if level == 'major':
            major, chapter = code, None
        elif level == 'intermediate':
            if row['parent_code'] != major:
                raise ValueError(f'Chapter outside its original part: {code}')
            chapter = code
        elif level == 'general_leaf':
            if row['parent_code'] != major or chapter is not None:
                raise ValueError(f'General item must precede chapters in its own part: {code}')
        elif row['parent_code'] != chapter or code[:2] != major[:2]:
            raise ValueError(f'Subject item outside its original chapter: {code}')
        seen.append(code)
    if len(seen) != len(set(seen)):
        raise ValueError('Duplicate codes in generated catalog')
    if set(seen) != set(source):
        raise ValueError({'missing': sorted(set(source) - set(seen)),
                          'unexpected': sorted(set(seen) - set(source))})
    if dict(counters) != {'部分': 63, '节': 6006, '章': 534}:
        raise ValueError(f'Wrong output counts: {counters}')
    return {'heading_counts': dict(counters), 'total_codes': len(seen),
            'unique_codes': len(set(seen)), 'codeset_sha256': code_hash(seen),
            'all_source_codes_preserved': True, 'no_duplicate_codes': True,
            'original_parent_relationships_preserved': True,
            'general_sections_before_chapters': True,
            'global_numbering_contiguous': True}



def payload_hash(payload: dict) -> str:
    return sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True,
                             separators=(',', ':')).encode('utf-8')).hexdigest()


def checked_titles(args, taxonomy, records) -> tuple[dict, dict, str]:
    """Restore source typography, or validate the distributed heading-only cache."""
    source_codes = {row['code'] for row in records}
    taxonomy_hash = file_hash(args.taxonomy)
    source_hash = taxonomy['source_sha256']
    if args.pdf.is_file():
        if file_hash(args.pdf) != source_hash:
            raise ValueError('PDF does not match the taxonomy source SHA-256')
        plain, pages = read_pdf_headings(args.pdf)
        if set(plain) != source_codes:
            raise ValueError('PDF and taxonomy heading-code sets disagree')
        if any(pages[row['code']] != row['pdf_page'] for row in records):
            raise ValueError('PDF page locations differ from the source index')
        import fitz
        with fitz.open(args.pdf) as doc:
            independent_codes = {
                match.group(1) for page in doc for line in page.get_text().splitlines()
                if (match := HEADING.match(line))
            }
            pages_count = len(doc)
        if independent_codes != source_codes:
            raise ValueError('Independent PyMuPDF code-set verification failed')
        if not set(MATH_TITLE_OVERRIDES) <= source_codes:
            raise ValueError('Unknown mathematical title code')
        titles = plain | MATH_TITLE_OVERRIDES
        for code, change in NAME_NORMALIZATIONS.items():
            if change['before'] not in titles[code]:
                raise ValueError(f'Expected source name not found: {code}')
            titles[code] = titles[code].replace(change['before'], change['after'])
        cache = {
            'schema_version': 1,
            'scope': 'Classification names only, with original code and PDF page; no textbook or source explanatory paragraphs. No original PDF redistribution or open license is implied.',
            'source_pdf_sha256': source_hash,
            'source_pdf_pages': pages_count,
            'source_taxonomy_sha256': taxonomy_hash,
            'source_codeset_sha256': code_hash(source_codes),
            'independent_pdf_engine_codeset_sha256': code_hash(independent_codes),
            'entries': [
                {'code': row['code'], 'pdf_page': row['pdf_page'],
                 'title_plain_extracted': plain[row['code']],
                 'title_markdown': titles[row['code']]}
                for row in records
            ],
            'math_title_restorations': [
                {'code': code, 'source_pdf_page': pages[code],
                 'original_extracted_title': plain[code],
                 'verified_markdown_title': title,
                 'verification': ('Rendered source PDF crop visually inspected; mathematical positioning and glyphs restored.'
                                  if code in VISUALLY_REVIEWED_MATH_CODES else
                                  'Source PDF embedded mathematical font spans inspected; ordinary mathematical Latin tokens restored.')}
                for code, title in sorted(MATH_TITLE_OVERRIDES.items())
            ],
            'name_normalizations': NAME_NORMALIZATIONS,
        }
        cache['cache_payload_sha256'] = payload_hash(cache)
        args.cache.parent.mkdir(parents=True, exist_ok=True)
        args.cache.write_text(json.dumps(cache, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        mode = 'source_pdf_and_verified_title_cache'
    else:
        cache = json.loads(args.cache.read_text(encoding='utf-8'))
        digest = cache.get('cache_payload_sha256')
        if digest != payload_hash({key: value for key, value in cache.items() if key != 'cache_payload_sha256'}):
            raise ValueError('Title cache payload SHA-256 verification failed')
        if cache.get('schema_version') != 1:
            raise ValueError('Unsupported title cache schema')
        if cache.get('source_pdf_sha256') != source_hash or cache.get('source_taxonomy_sha256') != taxonomy_hash:
            raise ValueError('Title cache source identity does not match taxonomy')
        cached_rows = cache['entries']
        if len(cached_rows) != len(source_codes) or {row['code'] for row in cached_rows} != source_codes:
            raise ValueError('Title cache has missing, duplicate, or unexpected codes')
        expected_codes_hash = code_hash(source_codes)
        if any(cache.get(key) != expected_codes_hash for key in
               ('source_codeset_sha256', 'independent_pdf_engine_codeset_sha256')):
            raise ValueError('Title cache code-set hash mismatch')
        page_map = {row['code']: row['pdf_page'] for row in records}
        if any(row['pdf_page'] != page_map[row['code']] for row in cached_rows):
            raise ValueError('Title cache page provenance mismatch')
        titles = {row['code']: row['title_markdown'] for row in cached_rows}
        if any(titles.get(code) != title for code, title in MATH_TITLE_OVERRIDES.items()):
            raise ValueError('Title cache does not match verified mathematical heading map')
        mode = 'verified_title_cache_without_source_pdf'
    if any(not title or title.count('$') % 2 for title in titles.values()):
        raise ValueError('Empty title or unpaired mathematical delimiters')
    # Non-ASCII math glyphs must be explicitly rendered, never left as damaged text.
    for code, title in titles.items():
        prose = re.sub(r'\$[^$]+\$', '', title)
        if re.search(r'[\u0370-\u03ff\u2200-\u22ff]', prose):
            raise ValueError(f'Unformatted mathematical glyph in {code}: {prose}')
    return titles, cache, mode


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--taxonomy', type=Path, default=ROOT/'data/msc_taxonomy.json')
    parser.add_argument('--pdf', type=Path, default=DEFAULT_PDF)
    parser.add_argument('--output', type=Path, default=ROOT/'dist/综合数学_完整数学目录.md')
    parser.add_argument('--validation', type=Path, default=ROOT/'data/catalog_validation.json')
    parser.add_argument('--cache', type=Path, default=ROOT/'data/catalog_titles.json')
    parser.add_argument('--translations', type=Path, default=ROOT/'data/catalog_titles_zh.json')
    args = parser.parse_args()
    taxonomy = json.loads(args.taxonomy.read_text(encoding='utf-8'))
    records = taxonomy['entries']
    source_codes = [row['code'] for row in records]
    if len(source_codes) != len(set(source_codes)):
        raise ValueError('Taxonomy contains duplicate codes')
    counts = dict(Counter(row['level'] for row in records))
    if counts != EXPECTED:
        raise ValueError(f'Unexpected taxonomy counts: {counts}')
    titles, cache, verification_mode = checked_titles(args, taxonomy, records)
    translated = json.loads(args.translations.read_text(encoding='utf-8'))
    if translated['source_title_cache_sha256'] != file_hash(args.cache):
        raise ValueError('Chinese translation source cache does not match current source')
    translation_rows = translated['entries']
    if len(translation_rows) != len(records) or {r['code'] for r in translation_rows} != set(source_codes):
        raise ValueError('Incomplete or duplicate Chinese heading translations')
    display_titles = {r['code']: r['title_zh'] for r in translation_rows}
    parents = {r['code']:r['parent_code'] for r in records}
    for item in translation_rows:
        code = item['code']
        if item['title_en'] != titles[code] or item['parent_code'] != parents[code]:
            raise ValueError(f'Translation source or hierarchy mismatch: {code}')
        if not re.search(r'[\u4e00-\u9fff]', item['title_zh']):
            raise ValueError(f'Missing Chinese title: {code}')
        if re.findall(r'\$[^$]+\$', titles[code]) != re.findall(r'\$[^$]+\$', item['title_zh']):
            raise ValueError(f'Mathematical notation changed in translation: {code}')
    children = defaultdict(list)
    for row in records:
        children[row['parent_code']].append(row)
    text = [
        '**《综合数学》完整数学目录**', '', '**著作人：Leo Lee**', '',
        '本目录列出全书的编写范围，含 63 个部分、534 个章节、6006 个节项；不表示这些内容已全部写成教材。'
        '503 个通用文献类型节项直接列在各部分开头，其后按原有 534 个中级类别列章，并列出 5503 个专门主题节项。'
        '不为通用条目虚构章节。', '',
        '本目录按 MSC2020 分类顺序编排，保留全部代码及归属，作为主题定位与编写范围索引。'
        '分类顺序不等于学习顺序，各节可按完整教学、专题展开或导读定位编写；先修路径另行安排。'
        '各级标题均采用中文；经作者同意，第1章使用“绪论：一般与综合专题”，对应00Axx。'
        '中文标题为本书译名，英文对照保存在伴生台账中；数学记号与分类代码保留。'
        '标题仅保留分类名称，去除交叉检索提示并恢复换行断词及经原页核验的数学排版，不含大段原文或新增教材内容。', '',
        '分类依据：《数学评论》与《数学文摘》编制的MSC2020，用户提供的224页附件。'
        '本目录属于分类定位索引，不构成对原始 PDF 或其他来源正文的开放授权；不随目录重发原始 PDF。', ''
    ]
    part_number = chapter_number = section_number = 0
    restored = []
    reflowed = []
    for row in records:
        if row.get('title_truncated'):
            restored.append({'code': row['code'], 'full_title': titles[row['code']],
                             'original_short_length': len(row['title_short']),
                             'restored_length': len(titles[row['code']])})
        if titles[row['code']] != unicodedata.normalize('NFC', row['title_short']):
            reflowed.append(row['code'])
    for major in children[None]:
        if major['level'] != 'major' or not major.get('title_zh'):
            raise ValueError(f'Invalid major classification: {major}')
        part_number += 1
        text += [f"# 第{part_number}部分 {display_titles[major['code']]}（MSC {major['code']}）", '']
        direct = children[major['code']]
        for item in direct:
            if item['level'] != 'general_leaf':
                continue
            section_number += 1
            text += [f"### 第{section_number}节 {display_titles[item['code']]}（{item['code']}）", '']
        for chapter in direct:
            if chapter['level'] != 'intermediate':
                continue
            chapter_number += 1
            chapter_title = "绪论：一般与综合专题" if chapter["code"] == "00Axx" else display_titles[chapter["code"]]
            text += [f"## 第{chapter_number}章 {chapter_title}（{chapter['code']}）", '']
            for item in children[chapter['code']]:
                if item['level'] != 'subject_leaf':
                    raise ValueError(f'Unexpected child: {item}')
                section_number += 1
                text += [f"### 第{section_number}节 {display_titles[item['code']]}（{item['code']}）", '']
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text('\n'.join(text), encoding='utf-8')
    checks = verify_catalog(args.output, records)
    validation = {
        'status': 'passed', 'source_pdf_sha256': cache['source_pdf_sha256'],
        'verification_mode': verification_mode,
        'independent_pdf_verification_performed_this_run': args.pdf.is_file(),
        'title_cache_sha256': file_hash(args.cache),
        'title_cache_payload_sha256': cache['cache_payload_sha256'],
        'math_title_restoration_count': len(cache['math_title_restorations']),
        'visually_reviewed_math_title_count': len(VISUALLY_REVIEWED_MATH_CODES),
        'math_title_restorations': cache['math_title_restorations'],
        'name_normalizations': NAME_NORMALIZATIONS,
        'source_pdf_pages': cache['source_pdf_pages'], 'source_taxonomy_sha256': file_hash(args.taxonomy),
        'catalog_sha256': file_hash(args.output), 'generator_sha256': file_hash(Path(__file__)),
        'source_counts': counts, 'catalog_checks': checks,
        'independent_pdf_engine_codeset_sha256': cache['independent_pdf_engine_codeset_sha256'],
        'recorded_independent_pdf_engine_matches_source_and_catalog': True,
        'titles_restored_from_truncated_index': restored,
        'reflowed_or_restored_title_codes': reflowed,
        'title_processing': 'Full PDF headings; routing cross-references removed; line-end word breaks restored; genuine lexical hyphens preserved; NFC Unicode normalization; per-code mathematical typography restored from source pages with verification provenance in the title cache. No title-length truncation. Cache hashes check integrity and source identity, not legal permission or independent authentication.',
        'scope': 'Complete mathematical writing catalog only; not a declaration of completed textbook chapters or source-text reuse rights.',
        'catalog_language': 'zh-CN',
        'chinese_translation_count': len(display_titles),
        'chinese_translation_file_sha256': file_hash(args.translations),
    }
    args.validation.parent.mkdir(parents=True, exist_ok=True)
    args.validation.write_text(json.dumps(validation, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': 'passed', 'output': str(args.output),
                      'parts': part_number, 'chapters': chapter_number, 'sections': section_number,
                      'restored_truncated_titles': len(restored),
                      'catalog_sha256': validation['catalog_sha256']}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
