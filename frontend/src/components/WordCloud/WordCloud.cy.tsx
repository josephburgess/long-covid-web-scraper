import WordCloud from './WordCloud';
import { mount } from '@cypress/react18';

describe('<WordCloud />', () => {
  beforeEach(() => {
    cy.fixture('sample_wordcloud_data.json').then((wordData) => {
      cy.intercept('GET', '/api/wordcloud', {
        fixture: 'sample_wordcloud_data.json',
      }).as('fetchWordCloudData');
    });

    mount(<WordCloud onWordClick={() => {}} />);
  });

  it('displays words once the data is fetched', () => {
    cy.wait('@fetchWordCloudData');
    cy.contains('word1').should('be.visible');
    cy.contains('word2').should('be.visible');
    cy.contains('word3').should('be.visible');
  });

  it('triggers onWordClick callback when a word is clicked', () => {
    const onWordClick = cy.stub().as('onWordClick');
    mount(<WordCloud onWordClick={onWordClick} />);

    cy.wait('@fetchWordCloudData');
    cy.contains('word1').click();

    cy.get('@onWordClick').should('be.calledOnce');
  });
});
