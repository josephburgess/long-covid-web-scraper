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
    cy.get('[data-cy="news-article"]').should('have.length', 3);
  });

});
