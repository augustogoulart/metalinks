import {mount} from "@vue/test-utils";
import LinkList from "@/components/LinkList.vue";

describe('LinkList', () => {
  test('is a Vue instance', () => {
    const wrapper = mount(LinkList);
    expect(wrapper.isVueInstance()).toBeTruthy()
  })

  test('has links property', () => {
    const wrapper = mount(LinkList);
    wrapper.setProps({ links: [] });
    expect(wrapper.props().links).toBeTruthy()
  })
});
