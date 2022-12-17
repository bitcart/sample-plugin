import ErrorLayout from "@TestPage/components/ErrorLayout.vue"
import ExtraStep from "@TestPage/components/ExtraStep.vue"
import NewCard from "@TestPage/components/NewCard.vue"

export default {
  extendComponents: {
    // cart_product_actions: [NewCard],
    // empty_cart: [NewCard],
    // success_cart: [SuccessCart],
    // checkout_enter_details: [NewCard],
    // checkout_enter_details_extra: [NewCard],
    // checkout: [NewCard],
    // checkout_tab_item: [NewCard],
    // checkout_empty: [NewCard],
    // checkout_status_display: [NewCard],
    // app: [NewCard],
    // header: [NewCard],
    // body: [NewCard],
    // footer: [NewCard],
    // cart_sidebar: [NewCard],
    error: [ErrorLayout],
    // cart: [NewCard],
    // step_menu: [NewCard],
    // cart_products: [NewCard],
    cart_steps_extra: [ExtraStep],
    // home_page: [NewCard],
    main_hero: [NewCard],
    // sidebar: [NewCard],
    // products: [NewCard],
    // pagination: [NewCard],
    // product: [NewCard],
    // product_image: [NewCard],
    // product_description: [NewCard],
  },
  dictionaries: {
    head: { title: "Modified via plugin" },
    product_head: { title: "Modified via plugin" },
    checkout_status_texts: {},
    step_menu: [
      {
        title: "Post-verify",
        icon: "fa-flask",
      },
    ],
  },
}
