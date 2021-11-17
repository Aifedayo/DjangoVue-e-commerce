<template>
  
</template>

<script>
export default {
    name: 'MyAccount',

    methods: {
        logout() {
            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")
            
            this.$store.commit('removeToken')

            this.$routr.push('/')
        }
    }
}
</script>

<style>

</style>