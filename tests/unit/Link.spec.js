import { mount } from '@vue/test-utils'
import Link from '@/components/Link.vue'
import LinkList from '@/components/LinkList.vue'

describe('Link', () => {
  test('is a Vue instance', () => {
    const wrapper = mount(Link);
    expect(wrapper.isVueInstance()).toBeTruthy()
  })
});

