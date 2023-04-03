import React from 'react';
import RedditPost from './RedditPost';
import { mount } from '@cypress/react18';

describe('<RedditPost />', () => {
  const post = {
    title: 'Test post',
    url: 'https://www.reddit.com/test-post',
    created: Date.now() / 1000,
  };

  it('renders', () => {
    mount(<RedditPost title={post.title} url={post.url} created={post.created} />);
  });

  it('displays the post title', () => {
    mount(<RedditPost title={post.title} url={post.url} created={post.created} />)
    cy.get('[data-cy="title"]').should('contain.text', 'Test post');
  });

  it('displays the post URL', () => {
    mount(<RedditPost title={post.title} url={post.url} created={post.created} />)
      .get('[data-cy="title"]')
      .should('have.attr', 'href', post.url);
  });

  it('displays a thumbnail image', () => {
    mount(<RedditPost title={post.title} url={post.url} created={post.created} />)
      .get('[data-cy="thumbnail"]')
      .should('be.visible');
  });

  it('displays the timestamp', () => {
    mount(<RedditPost title={post.title} url={post.url} created={post.created} />)
      .get('[data-cy="timestamp"]')
      .should('be.visible');
  });
});
