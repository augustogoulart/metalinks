<template>
  <section>
    <Navbar />
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
}
</script>

<style>
html{
  background-color: #FBFAFF;
}
</style>
