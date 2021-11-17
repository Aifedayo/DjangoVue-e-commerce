<template>
    <div class="page-content">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            zipcodes: '',
            place: '',
            errors: []
        }
    },

    mounted() {
        document.title = 'Checkout | zedEX'

        this.cart = this.$store.state.cart
    },

    
}
</script>

<style>

</style>