<template>
    <div class="container mx-auto">
      <Link v-for="link in links"
            key="link.id"
            :url="link.url"
            :category="link.category"
            :title="link.title"
            :description="link.description"
      />
    </div>
</template>

<script>
import Link from '~/components/Link'

export default {
  name: 'LinkList',
  components: {
    Link
  },
  props: {
    links: Array
  },
}
</script>

<style scoped>
</style>
