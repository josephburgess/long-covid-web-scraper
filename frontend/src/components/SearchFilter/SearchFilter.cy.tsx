import SearchFilter from './SearchFilter';
import { mount } from '@cypress/react18';

describe('<SearchFilter />', () => {
  const searchTerms = [
    { value: 'term1', label: 'Term 1' },
    { value: 'term2', label: 'Term 2' },
    { value: 'term3', label: 'Term 3' },
  ];

  it('renders', () => {
    mount(<SearchFilter onChange={() => {}} searchTerms={searchTerms} />);
  });

  it('displays search term options', () => {
    mount(<SearchFilter onChange={() => {}} searchTerms={searchTerms} />);

    cy.get('.search-filter__dropdown-indicator').click();

    searchTerms.forEach(({ label }) => {
      cy.get('.search-filter__option').contains(label).should('be.visible');
    });
  });

  it('selects and removes search terms', () => {
    const onChange = cy.stub().as('onChange');
    mount(<SearchFilter onChange={onChange} searchTerms={searchTerms} />);

    cy.get('.search-filter__dropdown-indicator').click();
    cy.get('.search-filter__option').contains(searchTerms[0].label).click();

    cy.get('@onChange')
      .should('be.calledOnce')
      .and('be.calledWith', [searchTerms[0]]);

    cy.get('.search-filter__multi-value__remove').click();

    cy.get('@onChange').should('be.calledTwice').and('be.calledWith', []);
  });

  it('creates and selects a new search term', () => {
    const newTerm = { value: 'term4', label: 'Term 4' };
    const onChange = cy.stub().as('onChange');
    mount(<SearchFilter onChange={onChange} searchTerms={searchTerms} />);

    cy.get('.search-filter__dropdown-indicator').click();
    cy.get('.search-filter__input').type(`${newTerm.label}{enter}`);

    cy.get('@onChange').should('have.been.calledOnce');
  });
});
