<template>
  <section>
    <Navbar />
      <LinkList />
  </section>
</template>

<script>
import LinkList from '@/components/LinkList'
import Navbar from '@/components/Navbar'

export default {
  components: {
    LinkList,
    Navbar
  }
}
</script>
