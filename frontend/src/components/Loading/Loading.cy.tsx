import Loading from './Loading'
import { mount } from '@cypress/react18';

describe('<Loading />', () => {
  it('renders', () => {
    mount(<Loading />)
  })
})