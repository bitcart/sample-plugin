<template lang="pug">
.has-text-centered
  h2 Success!
  p Your order has been processed, it will be delivered shortly.
  button.button(@click="setActualStep(3)") Next
</template>

<script>
import { createNamespacedHelpers } from "vuex"

const { mapActions } = createNamespacedHelpers("cart")

export default {
  methods: {
    ...mapActions(["setActualStep"]),
  },
}
</script>
