import LinkService from '@/services/LinkService'

export const state = () => ({
  links: []
});

export const mutations = {
  SET_LINKS(state, links) {
    state.links = links
  }
};

export const actions = {
  fetchLinks({commit}) {
    return LinkService.getLinks().then(response => {
      commit('SET_LINKS', response.data)
    })
  }
};

export const getters = {
  getList: state => {
    return state.links
  }
};
