<template>
  <div class="bg-white my-4 shadow p-8 rounded-lg md:flex">
    <div class="md:flex-shrink-0">
    <img class="rounded-lg md:w-24" src="https://github.githubassets.com/images/modules/logos_page/Octocat.png"
         alt="GitHub logo">
  </div>
  <div class="mt-4 md:mt-0 md:ml-6">
    <div class="uppercase tracking-wide text-sm text-indigo-600 font-bold">{{category}}</div>
    <a href="#" class="block mt-1 text-lg leading-tight font-semibold text-gray-900 hover:underline">{{title}}</a>
    <p class="mt-2 text-gray-600">{{description}}</p>
    <a :href="url">{{url}}</a>
  </div>
  </div>
</template>

<script>
  export default {
    name: 'Link',
    props:{
      url: String,
      category: String,
      title: String,
      description: String
    }
  }

</script>
