<template>
  <section>
    <Navbar />
    <div>
      {{getList}}
    </div>
      <LinkList />
  </section>
</template>

<script>
import LinkList from '@/components/LinkList'
import Navbar from '@/components/Navbar'
import {mapGetters} from 'vuex';
import axios from 'axios';

export default {

  async fetch ({ store }) {
    let baseUrl = 'https://djx-involved.herokuapp.com/api/links/';
    let { data } = await axios.get(baseUrl);
    store.commit('link/setLinks', data)
  },
  components: {
    LinkList,
    Navbar
  },
  computed:{
    ...mapGetters({
      getList: 'link/getList'
    })
  }
}
</script>

<style>
html{
  background-color: #FBFAFF;
}
</style>
