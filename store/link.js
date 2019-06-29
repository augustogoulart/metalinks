export const state = () => ({
  links: []
});

export const mutations = {
  setLinks: (state, links) => {
    state.links = links
  }
};

export const actions = {
  setLinks: (context, links) => {
    context.commit('setLinks', links)
  }
};

export const getters = {
  getList: state => {
    return state.links
  }
};
