// cypress/component/Navbar.spec.ts
import Navbar from "./Navbar";
import { mount } from '@cypress/react18';
import { BrowserRouter as Router } from 'react-router-dom';

describe('<Navbar />', () => {
  beforeEach(() => {
    mount(
      <Router>
        <Navbar />
      </Router>
    );
  });

  it('displays the correct navigation links', () => {
    cy.get('[data-cy="navbar"]').should('be.visible');
    cy.get('[data-cy="navbar-title"]').contains('Long COVID Hub');
    cy.get('[data-cy="navbar-link-news"]').contains('News');
    cy.get('[data-cy="navbar-link-data"]').contains('Research');
    cy.get('[data-cy="navbar-link-reddit"]').contains('Reddit Feed');
  });
});
