import React from 'react'
import RedditFeed from './RedditFeed'

describe('<RedditFeed />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-react
    cy.mount(<RedditFeed />)
  })
})