
const app = Vue.createApp({
	data() {
		return {
			progressrating: 0
		}
	}
})
app.component('star-rating', VueStarRating.default)
app.mount('#app')