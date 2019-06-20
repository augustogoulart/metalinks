<template>
  <section>
    <h1>Involved</h1>
    <div class="container">
      <Link />
      <Link />
      <Link />
      <Link />
      <Link />
      <Link />
    </div>
  </section>
</template>

<script>
import Link from '~/components/Link'

export default {
  components: {
    Link
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
