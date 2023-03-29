import React from 'react'
import RedditFeed from './RedditFeed'
import { mount } from '@cypress/react18';

describe('<RedditFeed />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-react
    mount(<RedditFeed />)
  })
})