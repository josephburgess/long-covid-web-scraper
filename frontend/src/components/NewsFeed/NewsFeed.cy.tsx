import React from 'react';
import NewsFeed from './NewsFeed';
import { mount } from '@cypress/react18';
import sampleNews from '../../../cypress/fixtures/sample_news.json';

describe('<NewsFeed />', () => {
  beforeEach(() => {
    cy.intercept('/api/news', sampleNews).as('getNews');
    mount(<NewsFeed />);
    cy.wait('@getNews');
  });

  it('renders', () => {});

  it('displays the correct page title', () => {
    cy.contains('h1', 'News Feed').should('be.visible');
  });

  it('displays a list of news articles', () => {
    cy.get('li').should('have.length', 3);
  });

  it('displays the correct article headline and link', () => {
    cy.get('li')
      .eq(0)
      .within(() => {
        cy.get('a')
          .should(
            'have.attr',
            'href',
            'https://www.theguardian.com/society/2023/mar/27/long-covid-two-thirds-workers-unfair-treatment-report'
          )
          .should(
            'have.text',
            'Two-thirds of UK workers with long Covid have faced unfair treatment, says report'
          );
      });
  });
});
