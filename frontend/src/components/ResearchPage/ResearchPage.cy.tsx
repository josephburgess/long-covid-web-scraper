import React from 'react'
import ResearchPage from './ResearchPage'
import { mount } from '@cypress/react18';

describe('<ResearchPage />', () => {
  it('renders correctly with initial selection', () => {
    mount(<ResearchPage />);
    cy.get('h1').contains('Research');
    cy.get('[data-cy="research-sidebar"]').should('exist');
    cy.get('[data-cy="research-feed"]').should('exist');
    cy.get('[data-cy="year-published-graph"]').should('not.exist');
  });

  it('changes selection when clicking buttons on sidebar', () => {
    mount(<ResearchPage />);
    
    cy.get('button').contains('Publication Tracker').click();
    cy.get('[data-cy="research-feed"]').should('not.exist');
    cy.get('[data-cy="year-published-graph"]').should('exist');

    cy.get('button').contains('Research Feed').click();
    cy.get('[data-cy="research-feed"]').should('exist');
    cy.get('[data-cy="year-published-graph"]').should('not.exist');
  });
});
