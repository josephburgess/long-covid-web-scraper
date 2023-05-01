import ResearchFeed from './ResearchFeed';
import { mount } from '@cypress/react18';

describe('<ResearchFeed />', () => {
  beforeEach(() => {
    cy.fixture('sample_research.json').then((articles) => {
      cy.intercept('GET', 'http://127.0.0.1:5000/api/data', {
        fixture: 'sample_research.json',
      }).as('fetchResearchArticleData');
      mount(<ResearchFeed searchFilter='' />);
    });
  });

  it('displays a loading indicator before the articles are fetched', () => {
    cy.get('[data-cy="loading-indicator"]').should('be.visible');
    cy.get('[data-cy="research-article"]').should('not.exist');
  });

  it('displays Research articles once they are fetched', () => {
    cy.wait('@fetchResearchArticleData');
    cy.get('[data-cy="loading-indicator"]').should('not.exist');
    cy.get('[data-cy="research-article"]').should('have.length.at.least', 1);
  });
});
