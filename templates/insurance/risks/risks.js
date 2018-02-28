// Vue.component('todo-item', {
//   // The todo-item component now accepts a
//   // "prop", which is like a custom attribute.
//   // This prop is called todo.
//   props: ['todo'],
//   template: '<li>{{ todo.text }}</li>'
// });

// import Vue from 'vue';
// import VueMonthlyPicker from 'vue-monthly-picker';

Vue.component('date-field', {
    components: {
        'vue-monthly-picker'
    }
});

Vue.component('text-field', {
  template: '<textarea></textarea>'
});

new Vue({
    delimiters: ['[[', ']]'],
    el: '#risks-app',
    data: {
      risks: ['r1', 'r2', 'r2']
    }
});

