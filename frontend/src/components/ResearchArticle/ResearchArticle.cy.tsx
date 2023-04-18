import { mount } from '@cypress/react18';
import ResearchArticle from './ResearchArticle'

describe('<ResearchArticle />', () => {
  const article = {
    title: 'Test article',
    source: 'BMJ',
    publication_date: '2021-Mar-01',
    authors: 'Test Author, Test Author',
    url: 'https://www.bmj.com/test-article',
  };

  beforeEach(() => {
    mount(<ResearchArticle {...article} />);
  });

  it('renders', () => {
    cy.get('[data-cy="research-article"]').should('be.visible');
  })

  it('displays the article title', () => {
    cy.get('[data-cy="title"]').should('contain.text', article.title);
  })

  it('displays the article URL', () => {
    cy.get('[data-cy="title"]')
      .should('have.attr', 'href', article.url);
  })
  
  it('displays the article source', () => {
    cy.get('[data-cy="source"]').should('contain.text', article.source);
  })

  it('displays the article publication date', () => {
    cy.get('[data-cy="publication_date"]').should('contain.text', article.publication_date);
  })

  it('displays the article authors', () => {
    cy.get('[data-cy="authors"]').should('contain.text', article.authors);
  })
})