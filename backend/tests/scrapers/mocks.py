def mock_summarise_text(text):
    return "Sample summary"


pubmed_url = 'https://pubmed.ncbi.nlm.nih.gov/?term=("long+covid")+NOT+Corrigendum&filter=simsearch1.fha&filter=pubt.booksdocs&filter=pubt.clinicaltrial&filter=pubt.meta-analysis&filter=pubt.randomizedcontrolledtrial&filter=pubt.review&filter=pubt.systematicreview&format=abstract&size=50&page=1'
sample_pubmed_html = """
<div class="results-article">
    <h1 class="heading-title">
    <a href="/12345678/">Sample Article Title</a>
    <span class="authors-list">John Doe, Jane Smith</span>
    <span class="cit">Jan 01, 2022</span>
    <div class="abstract-content">
        <p>Sample abstract text</p>
    </div>
</div>
"""

sample_pubmed_html_no_abstract = """
<div class="results-article">
    <h1 class="heading-title">
    <a href="/12345678/">Sample Article Title</a>
    <span class="authors-list">John Doe, Jane Smith</span>
    <span class="cit">Jan 01, 2022</span>
</div>
"""

sample_pubmed_html_multi_para_abstract = """
<div class="results-article">
    <h1 class="heading-title">
    <a href="/12345678/">Sample Article Title</a>
    <span class="authors-list">John Doe, Jane Smith</span>
    <span class="cit">Jan 01, 2022</span>
    <div class="abstract-content">
        <p>Sample abstract text</p>
        <p>Another paragraph of abstract</p>
    </div>
</div>
"""

sample_pubmed_html_no_citation = """
<div class="results-article">
    <h1 class="heading-title">
    <a href="/12345678/">Sample Article Title</a>
    <span class="authors-list">John Doe, Jane Smith</span>
    <div class="abstract-content">
        <p>Sample abstract text</p>
    </div>
</div>
"""

bmj_url = "https://www.bmj.com/search/advanced/title%3Along%2Bcovid%20title_flags%3Amatch-all%20numresults%3A100%20sort%3Apublication-date%20direction%3Adescending%20format_result%3Astandard"
sample_bmj_html = """
<div class="highwire-article-citation">
  <a href="www.example.com" class="highwire-cite-linked-title">Sample Article Title</a>
  <div  class="highwire-cite-authors"><span class="nlm-given-names">John</span> <span class="nlm-surname">Doe</span></div>
  <span  class="highwire-cite-metadata-date">Mar 01, 2023</span><span  class="highwire-cite-metadata-date">Mar 01, 2023</span>
</div>
"""


lancet_url = "https://www.thelancet.com/action/doSearch?text1=long+covid&field1=Title&journalCode=lancet&SeriesKey=lancet"
sample_lancet_html = """
<li class="search__item">
    <span class="hlFld-Title">
    <a href="/journals/lancet/article/PIIS0140-6736(23)X000X-X/fulltext" class="hlFld-Title" target="_self" >Long COVID: 3 years in</a>
    <ul class="meta__authors">
        <li>The Lancet</li>
    </ul>
    <span class="meta__date">
        <span class="meta__date__text" id="item_date">11 Mar 2023</span>
    </span>
</li>
<li class="search__item">
    <span class="hlFld-Title">
    <a href="/journals/lancet/article/PIIS0140-6736(23)X000X-X/fulltext" class="hlFld-Title" target="_self" >Healing Long Covid: a marathon not a sprint</a>
    <ul class="meta__authors">
        <li>Nisreen A Alwan</li>
    </ul>
    <span class="meta__date">
        <span class="meta__date__text" id="item_date">4 Mar 2023</span>
    </span>
</li>

"""
