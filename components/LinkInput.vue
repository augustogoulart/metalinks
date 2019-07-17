<template>
  <div class="container mx-auto">
    <form @submit.prevent="onsubmit">
      <div class="my-4 pl-8 pr-8">
        <label class="block text-gray-700 text-sm font-bold"></label>
        <input v-model="link.url"
               class="shadow appearance-none border rounded w-full py-4 px-5 text-gray-700
          leading-tight focus:outline-none focus:shadow-outline"
               name='link' type="text" placeholder="Store a new url">
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "LinkInput",
  data() {
    return {
      link: {
        url: null
      }
    }
  },
  methods: {
    onsubmit() {
      this.$store.dispatch('links/addLink', this.link);
      this.clearInput()
    },
    clearInput() {
      this.link = {}
    }
  }
}
</script>
