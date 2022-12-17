<template>
  <div>Error occured: {{ error }}</div>
</template>

<script>
export default {
  props: {
    error: {
      type: Object,
      default: null,
    },
  },
}
</script>
