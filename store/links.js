import LinkService from '@/services/LinkService'

export const state = () => ({
  links: []
});

export const mutations = {
  SET_LINKS(state, links) {
    state.links = links
  },
  ADD_LINK(state, link) {
    state.links = [...state.links, link]
  }
};

export const actions = {
  fetchLinks({commit}) {
    return LinkService.getLinks().then(response => {
      commit('SET_LINKS', response.data)
    })
  },
  addLink({commit}, link) {
    return LinkService.postLink(link).then(response => {
      commit('ADD_LINK', response.data)
    })
  }
};

export const getters = {
  getList: state => {
    return state.links
  }
};
