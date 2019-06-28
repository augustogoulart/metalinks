import {mount} from "@vue/test-utils";
import Navbar from "@/components/Navbar";

describe('Navbar', () => {
  const wrapper = mount(Navbar);

  test('is a Vue instance', () => {
    expect(wrapper.isVueInstance()).toBeTruthy()
  });

  test('shows Involved logo', () => {
    expect(wrapper.text()).toBe('Involved')
  })
});
