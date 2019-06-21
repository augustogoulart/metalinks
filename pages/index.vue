<template>
  <section>
    <h1>Involved</h1>
    <div class="container">
      <LinkList />
    </div>
  </section>
</template>

<script>
import LinkList from '~/components/LinkList'

export default {
  components: {
    LinkList
  }
}
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
