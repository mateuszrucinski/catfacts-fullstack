const app = Vue.createApp({
  data: function () {
    return {
      title: 'CatFacts',
      image: './assets/cat_face.png',
      number: '',
      text: '',
    }
  },
  methods: {
    async getFacts() {
      const response = await fetch(`http://127.0.0.1:8000/catfact/${this.number}`);
      const data = await response.json();
      this.text = data
    },
    }
}
)
