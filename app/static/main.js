const { createApp } = Vue

const TaskApp = {
    data(){
        return{
            task: {
                'title': ' '
            },
            tasks: []
        }
    },
    async created(){
        await this.getTasks()
    },
    methods:{
        async getTasks(){
            const response = await fetch(window.location, {
                method: 'get',
                headers:{
                    'X-Requested-With': 'XMLHttpRequets'
                }
            })
            this.tasks = await response.json()
        },
        async createTask(){
            await this.getTasks()
            const response = await fetch(window.location.origin + '/create', {
                method: 'post',
                headers:{
                    'Content-Type':'application/json',
                    'X-Requested-With': 'XMLHttpRequets'
                },
                body:JSON.stringify(this.task)
            })
            await this.getTasks()
        }
    },
    delimiters: ['{','}']
}

createApp(TaskApp).mount('#app')