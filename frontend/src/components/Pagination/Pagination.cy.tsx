import React from 'react';
import Pagination from './Pagination';
import { mount } from '@cypress/react18';

describe('<Pagination />', () => {
  const pageCount = 5;
  let onPageChangeMock: any;

  beforeEach(() => {
    onPageChangeMock = cy.stub();
    mount(
      <Pagination pageCount={pageCount} onPageChange={onPageChangeMock} />
    );
  });

  it('renders the Pagination component', () => {
    cy.get('.Pagination_pagination__vcNDC').should('be.visible');
  });

  it('renders the correct number of page buttons', () => {
    cy.get('.Pagination_pagination__vcNDC li').should('have.length', pageCount + 2);
  });

  it('clicks the next button and triggers onPageChange', () => {
    cy.get('li.next').click();
    cy.wrap(onPageChangeMock).should('have.been.calledOnceWith', { selected: 1 });
  });

  it('clicks the previous button and triggers onPageChange', () => {
    cy.get('li.next').click();
    cy.get('li.previous').click();
    cy.wrap(onPageChangeMock).should('have.been.calledWith', { selected: 0 });
  });
});
