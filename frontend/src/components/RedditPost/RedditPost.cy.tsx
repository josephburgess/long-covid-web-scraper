import React from 'react';
import RedditPost from './RedditPost';
import { mount } from '@cypress/react18';

describe('<RedditPost />', () => {
  const post = {
    title: 'Test post',
    url: 'https://www.reddit.com/test-post',
    created: Date.now() / 1000,
  };

  beforeEach(() => {
    mount(<RedditPost title={post.title} url={post.url} created={post.created} />);
  });

  it('displays the post title', () => {
    cy.get('[data-cy="title"]').should('contain.text', post.title);
  });

  it('displays the post URL', () => {
    cy.get('[data-cy="title"]')
      .should('have.attr', 'href', post.url);
  });

  it('displays a thumbnail image', () => {
    cy.get('[data-cy="thumbnail"]')
      .should('be.visible');
  });

  it('displays the timestamp', () => {
    cy.get('[data-cy="timestamp"]')
      .should('be.visible');
  });
});
