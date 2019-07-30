import LinkService from '@/services/LinkService'
import MetaParserService from '@/services/MetaParserService'

export const state = () => ({
  links: []
});

export const mutations = {
  SET_LINKS(state, links) {
    state.links = links
  },
  ADD_LINK(state, link) {
    state.links = [link, ...state.links]
  }
};

export const actions = {
  fetchLinks({commit}) {
    return LinkService.getLinks().then(response => {
      commit('SET_LINKS', response.data)
    })
  },
  addLink({commit}, link) {

    //Mocking the payload until we have a proper
    // way for processing metadata form HTML pages

    MetaParserService.parseMetaData(link).then(
      parsedData => {
        LinkService.postLink(parsedData.data).then(
          response => commit('ADD_LINK', response.data))
      });
  }
};

export const getters = {
  getList: state => {
    return state.links
  }
};
