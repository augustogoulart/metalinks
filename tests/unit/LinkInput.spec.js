import { mount } from '@vue/test-utils'
import LinkInput from '@/components/LinkInput.vue'

describe('LinkInput', () => {
  const wrapper = mount(LinkInput);

  test('is a Vue instance', () => {
    expect(wrapper.isVueInstance()).toBeTruthy()
  });

  test('has input form', () => {
    expect(wrapper.contains("form")).toBe(true)
  })
});
