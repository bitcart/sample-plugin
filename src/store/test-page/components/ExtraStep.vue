<template lang="pug">
  div(v-if="actualStep === 3")
    h1 Extra step
    p Here you can add some extra step to checkout process
    nuxt-link(exact :to="getHomeURL")
      button.button Fill again your cart
</template>

<script>
import { createNamespacedHelpers } from "vuex"
const { mapGetters } = createNamespacedHelpers("cart")

export default {
  computed: {
    ...mapGetters(["actualStep"]),
    getHomeURL() {
      const storeID = this.$route.params.id
      return storeID
        ? { name: "store-id", params: { id: storeID } }
        : { name: "index" }
    },
  },
}
</script>
