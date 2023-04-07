import React from 'react'
import ResearchSidebar from './ResearchSidebar'
import { mount } from '@cypress/react18'

describe('<ResearchSidebar />', () => {
  it('renders correctly', () => {
    mount(<ResearchSidebar onSelection={() => {}} />);
    cy.get('button').should('have.length.greaterThan', 0);
    cy.get('button').eq(0).contains('Research Feed');
    cy.get('button').eq(1).contains('Publication Tracker');
  });

  it('changes selection when clicking buttons', () => {
    const onSelectionMock = cy.stub();
    mount(<ResearchSidebar onSelection={onSelectionMock} />);

    cy.get('button').eq(0).click();
    cy.wrap(onSelectionMock).should('have.been.calledWith', 'researchFeed');

    cy.get('button').eq(1).click();
    cy.wrap(onSelectionMock).should('have.been.calledWith', 'publicationTracker');
  });
});