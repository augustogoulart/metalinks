export const state = () => ({
  list: {'url': 'http://link.com'}
});

export const getters = {
  getList: state => {
    return state.list
  }
};
