import {shallowMount} from '@vue/test-utils'
import LinkInput from '@/components/LinkInput.vue'

describe('LinkInput', () => {
  const wrapper = shallowMount(LinkInput, {});

  test('is a Vue instance', () => {
    expect(wrapper.isVueInstance()).toBeTruthy()
  });

  test('has input form', () => {
    expect(wrapper.contains("form")).toBe(true)
  });

  test('form has input field', () => {
    expect(wrapper.contains("input")).toBe(true)
  });

  test('has data property', () => {
    expect(wrapper.vm.$data).toBeTruthy()
  });

  test('data property has link field', () => {
    expect(wrapper.vm.$data.link).toBeTruthy()
  });

  test('link field has url set to null', () => {
    expect(wrapper.vm.$data.link.url).toBe(null)
  });
});
