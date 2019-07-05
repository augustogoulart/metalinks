import { mount } from '@vue/test-utils'
import Link from '@/components/Link.vue'

describe('Link', () => {
  const wrapper = mount(Link);

  test('is a Vue instance', () => {
    expect(wrapper.isVueInstance()).toBeTruthy()
  });

  test('has url property', () => {
    wrapper.setProps({url: 'some-link-url'});
    expect(wrapper.props().url).toBeTruthy()
  });

  test('has category property', () => {
    wrapper.setProps({category: 'some-category'});
    expect(wrapper.props().category).toBeTruthy()
  });

  test('has title property', () => {
    wrapper.setProps({title: 'some-title'});
    expect(wrapper.props().title).toBeTruthy()
  })

  test('has description property', () => {
    wrapper.setProps({description: 'some-description'});
    expect(wrapper.props().description).toBeTruthy()
  })
});
