// Importa la función createApp de la librería Vue
const { createApp } = Vue

// Define el componente TaskApp
const TaskApp = {
    // Define la función data, que retorna un objeto con los datos del componente
    data(){
        return{
            task: {
                'title': ' '
            },
            tasks: []
        }
    },
    async created(){
        // Llama a la función getTasks para obtener las tareas de la base de datos
        await this.getTasks()
    },
    methods:{
        // Define la función sendRequest, que recibe una URL, un método y datos, y realiza una petición fetch
        async sendRequest(url, method, data){
            const myHeaders = new Headers({
                'Content-Type':'application/json',
                'X-Requested-With': 'XMLHttpRequets'
            })

            // Realiza la petición fetch
            const response = await fetch(url, {
                method: method,
                headers: myHeaders,
                body: data
            })
            return response
        },
        // Define la función getTasks, que obtiene las tareas de la base de datos
        async getTasks(){
            const response = await this.sendRequest(window.location, 'get')
            this.tasks = await response.json()
        },
        // Define la función createTask, que crea una nueva tarea
        async createTask(){
            await this.getTasks()
            const response = await this.sendRequest(window.location.origin + '/create', 'post', JSON.stringify(this.task))
            await this.getTasks()

            // Limpia el valor de la propiedad title de la tarea
            this.task.title = ''
        },
        // Define la función deteleTask, que elimina una tarea
        async deteleTask(task){
            await this.sendRequest(window.location.origin + '/delete', 'post', JSON.stringify(task))
            await this.getTasks()
        },
        // Define la función completeTask, que completa una tarea
        async completeTask(task){
            await this.sendRequest(window.location.origin + '/complete', 'post', JSON.stringify(task))
            await this.getTasks()
        }
    },
    delimiters: ['{','}']
}

// Crea la aplicación Vue y la monta en el elemento con el id "app"
createApp(TaskApp).mount('#app')