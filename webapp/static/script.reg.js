const App = {
	data() {
		return {
			check: true,
			siginbutton: 'Зарегистрироваться',
			loginbutton: 'Войти'
		}
	}
}
Vue.createApp(App).mount('#app')

function emailValidation(value) {
	let txt = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	return txt.test(value);
}

function checkEmail() {
	let email = document.form.email.value;
	if (emailValidation(email)) {
		window.alert("OK");
	} else {
		window.alert("Email is incorrect");
	}
}