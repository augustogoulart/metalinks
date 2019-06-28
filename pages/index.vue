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

export default {
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
