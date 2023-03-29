import React from 'react'
import NewsArticles from './NewsArticles'

describe('<NewsArticles />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-react
    cy.mount(<NewsArticles />)
  })
})