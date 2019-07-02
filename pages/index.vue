<template>
  <section>
    <Navbar />
    <div>
      {{links}}
    </div>
      <LinkList />
  </section>
</template>

<script>
import LinkList from '@/components/LinkList'
import Navbar from '@/components/Navbar'
import {mapState} from 'vuex'

export default {
  components: {
    LinkList,
    Navbar
  },
  async fetch({store, error}) {
    await store.dispatch('links/fetchLinks')
  },
  computed: mapState({
      links: state => state.links.links
  })
}
</script>

<style>
html{
  background-color: #FBFAFF;
}
</style>
