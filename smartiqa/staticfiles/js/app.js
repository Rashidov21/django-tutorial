const App = {
	data(){
		return {
			comment:true,
			times:false,
			icons:false
		}
	},
	methods: {
		show: function () {
			this.comment = false;
			this.times = true;
			this.icons = true;
		},
		hide: function() {
			this.comment = true;
			this.times = false;
			this.icons = false;
		}
	}
}
const app = Vue.createApp(App).mount("#app");