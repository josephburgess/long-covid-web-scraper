import React from 'react'
import { mount } from '@cypress/react18';
import YearPublishedGraph from './YearPublishedGraph'

describe('<YearPublishedGraph />', () => {

  beforeEach(() => {
    cy.fixture('sample_data.json').then((sampleData) => {
      cy.intercept('GET', '/api/data', { body: sampleData });
    });
  })

  it('renders the graph', () => {
    mount(<YearPublishedGraph />);
    cy.get('.plot-container.plotly').should('be.visible');
    cy.get('.legend').should('be.visible');
  });
})