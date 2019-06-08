<template>
  <section class="container">
    <div>
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
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
