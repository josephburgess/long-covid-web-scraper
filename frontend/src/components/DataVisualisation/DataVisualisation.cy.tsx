import React from 'react'
import DataVisualisation from './DataVisualisation'

describe('<DataVisualisation />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-react
    cy.mount(<DataVisualisation />)
  })
})