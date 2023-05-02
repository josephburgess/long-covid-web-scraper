import pandas as pd

mock_df = pd.DataFrame(
    {
        "title": [
            "Symptoms",
            "Infection",
            "Health",
        ],
        "summary": [
            "Symptoms",
            "Infection",
            "Health",
        ],
        "publication_date": ["2020 May 10", "Published 15 Jun 2021", None],
        "source": ["pubmed", "BMJ", "pubmed"],
    }
)

test_articles = [
    {
        "title": "Article 1",
        "publication_date": "2020 May 10",
        "source": "pubmed",
    },
    {
        "title": "Article 2",
        "publication_date": "Published 15 Jun 2021",
        "source": "BMJ",
    },
    {"title": "Article 3", "publication_date": None, "source": "pubmed"},
]
