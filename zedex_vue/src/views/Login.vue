<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title mt-6">Login</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>
            
                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Login</button>
                        </div>
                    </div>
                    <hr>
                    or <router-link to="/sign-up">Click here</router-link> to sign up!
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Login',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },

    mounted() {
        document.title = 'Login | zedEx'
    },

    methods: {
        async submitForm() {
            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password
            }
            // this.errors = []

            // if (this.username === '') {
            //     this.errors.push('The username is missing')
            // }
            // if (this.password === '') {
            //     this.errors.push('The password is too short or missing')
            // }
            // if (this.password !== this.password2) {
            //     this.errors.push('The password doesn\'t match')
            // }

            // if (!this.errors.length) {
            //     const formData = {
            //         username: this.username,
            //         password: this.password
            //     }

            await axios
                .post('/api/v1/token/login/', formData)
                .then(response => {
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)

                    axios.defaults.headers.common["Authorization"] = "Token " + token

                    localStorage.setItem("token", token)
                    const toPath = this.$route.query.to || '/cart'

                    this.$router.push(toPath)

                    // toast({
                    //     message: 'Account created! Please log in.',
                    //     type: 'is-success',
                    //     dismissible: true,
                    //     pauseOnHover: true,
                    //     duration: 2000,
                    //     position: 'bottom-right'
                    // })

                    // this.$router.push('/log-in')
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')

                        console.log(JSON.stringify(error))
                    }
                })
            }
        }
    }
</script>

<style>

</style>