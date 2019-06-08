import { mount } from '@vue/test-utils'
import Link from '@/components/Link'

const wrapper = mount(Link)

describe('Link', () => {
    test('is a Vue instance', () => {
      expect(wrapper.isVueInstance()).toBeTruthy()
    });

    test('Has title', () => {
      expect(wrapper.text()).toContain('Involved')
    });

  })
  