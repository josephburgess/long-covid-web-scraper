import React from 'react'
import NewsArticles from './NewsArticle'
import { mount } from '@cypress/react18';


describe('<NewsArticles />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-react
    mount(<NewsArticles />)
  })
})