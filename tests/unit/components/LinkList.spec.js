import {shallowMount,mount} from "@vue/test-utils";
import LinkList from "@/components/LinkList.vue";

describe('LinkList', () => {
  const wrapper = shallowMount(LinkList, {
    computed: {
      links() {
        return []
      }
    }
  });

  test('is a Vue instance', () => {
    expect(wrapper.isVueInstance()).toBeTruthy()
  })

});
