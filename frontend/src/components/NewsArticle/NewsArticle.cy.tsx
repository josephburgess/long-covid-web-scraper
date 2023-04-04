import React from 'react';
import NewsArticle from './NewsArticle';
import { mount } from '@cypress/react18';

describe('<NewsArticle />', () => {
  const article = {
    'webUrl': 'https://www.example.com/article1',
    'headline': 'Example Article 1',
    'thumbnail': 'https://www.example.com/thumbnail1',
    'standfirst': 'This is an example article',
    'date': "2023-04-03T13:37:48Z"
  };

  beforeEach(() => {
    mount(<NewsArticle webUrl={article.webUrl} headline={article.headline} thumbnail={article.thumbnail} standfirst={article.standfirst} date={article.date} />);
  });

  it('displays the article headline', () => {
    cy.get('[data-cy="headline"]')
      .should('contain.text', article.headline);
  });

  it('contains the webUrl', () => {
    cy.get('[data-cy="webUrl"]')
      .should('have.attr', 'href', article.webUrl);
  });

  it('displays a thumbnail image', () => {
    cy.get('[data-cy="thumbnail"]')
      .should('be.visible');
  });

  it('displays the timestamp', () => {
    cy.get('[data-cy="date"]')
      .should('be.visible');
  });

  it('displays the standfirst', () => {
    cy.get('[data-cy="standfirst"]')
      .should('be.visible');
  });
});
