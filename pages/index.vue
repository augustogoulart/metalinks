<template>
  <section>
    <Navbar />
    <div>
      {{data}}
    </div>
      <LinkList />
  </section>
</template>

<script>
import LinkList from '@/components/LinkList'
import Navbar from '@/components/Navbar'
import {mapGetters} from 'vuex';

export default {
  async asyncData({ $axios }) {
  const data = await $axios.$get('links/')
  return { data }
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
