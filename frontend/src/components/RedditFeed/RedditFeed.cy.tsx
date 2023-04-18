import React from 'react'
import RedditFeed from './RedditFeed'
import { mount } from '@cypress/react18';

describe('<RedditFeed />', () => {
  beforeEach(() => {
    cy.fixture('sample_posts.json').then((posts) => {
      cy.intercept('POST', 'http://127.0.0.1:5000/api/reddit', {
        fixture: 'sample_posts.json',
      }).as('fetchRedditPosts');
    });

    mount(<RedditFeed />);
  });

  it('displays the Reddit Feed title', () => {
    cy.get('[data-cy="reddit-feed-title"]').should('be.visible').contains('Reddit Feed');
  });

  it('displays a loading indicator before the posts are fetched', () => {
    cy.get('[data-cy="loading-indicator"]').should('be.visible');
    cy.get('[data-cy="reddit-post"]').should('not.exist');
  });

  it('displays Reddit posts once they are fetched', () => {
    cy.wait('@fetchRedditPosts');
    cy.get('[data-cy="loading-indicator"]').should('not.exist');
    cy.get('[data-cy="reddit-post"]').should('have.length.at.least', 1);
  });

  it('paginates through the Reddit posts', () => {
    cy.wait('@fetchRedditPosts');
    cy.get('[data-cy="reddit-post"]').should('have.length', 20);

    cy.get('li.next').click();
    cy.get('[data-cy="reddit-post"]').should('have.length', 5);

    cy.get('li.previous').click();
    cy.get('[data-cy="reddit-post"]').should('have.length', 20);
  });
})



  
