import React from 'react'
import YearPublishedGraph from './YearPublished'

describe('<YearPublishedGraph />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-react
    cy.mount(<YearPublishedGraph />)
  })
})