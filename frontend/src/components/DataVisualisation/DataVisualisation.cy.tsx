import React from 'react'
import DataVisualisation from './DataVisualisation'
import { mount } from '@cypress/react18';

describe('<DataVisualisation />', () => {
  it('renders', () => {
    mount(<DataVisualisation />)
  })
})