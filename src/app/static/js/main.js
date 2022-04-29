function alert(message, type) {
    const wrapper = document.createElement('div')
    wrapper.innerHTML = '<div class="alert alert-' + type + ' alert-dismissible" role="alert">' + message + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'

    $('#liveAlertPlaceholder').append(wrapper)
}

Vue.createApp({
    created() {
        this.getPersonData()
    },
    data() {
        return {
            pessoa: {
                id: null,
                nome: null,
                rg: '',
                cpf: '',
                data_nascimento: '',
                data_admissao: '',
                data_admissao_locale: '',
                funcao: '',
            },
            pessoas: [],
            formSubmitLabel: 'Cadastrar',
            sendingForm: false,
            deletingPerson: false,
            loadingPersonData: false,
        }
    },
    methods: {
        getPersonData() {
            this.loadingPersonData = true

            fetch('/pessoas')
                .then(data => {
                    if (!data.ok) {
                        throw Error(data.status)
                    }

                    return data.json()
                })
                .then(json => {
                    this.pessoas = json.data
                    this.loadingPersonData = false
                    window.scrollTo(0, 0)
                })
                .catch(error => alert(error))
        },
        submitForm() {
            this.sendingForm = true

            if (this.pessoa.id) {
                const options = {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: new URLSearchParams(new FormData(document.querySelector("form"))),
                }
                fetch(`/pessoas/${this.pessoa.id}`, options)
                    .then(data => {
                        this.sendingForm = false

                        if (!data.ok) {
                            throw new Error(data.status)
                        }

                        return data.json()
                    })
                    .then(pessoa => {
                        this.clearForm()
                        alert('Registro atualizado com sucesso', 'info')
                        this.getPersonData()
                    })
                    .catch(error => alert(error))
            } else {
                const options = {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: new URLSearchParams(new FormData(document.querySelector("form"))),
                }
                fetch('/pessoas', options)
                    .then(data => {
                        this.sendingForm = false

                        if (!data.ok) {
                            throw new Error(data.status)
                        }

                        return data.json()
                    })
                    .then(pessoa => {
                        this.clearForm()
                        alert('Registro cadastrado com sucesso', 'info')
                        this.getPersonData()
                    })
                    .catch(error => alert(error))
            }

        },
        clearForm() {
            this.pessoa = {
                id: null,
                nome: '',
                rg: '',
                cpf: '',
                data_nascimento: '',
                data_admissao: '',
                data_admissao_locale: '',
                funcao: '',
            }
            this.formSubmitLabel = 'Cadastrar'
        },
        updatePerson(pessoaId) {
            this.pessoa = this.pessoas.find(pessoa => pessoa.id === pessoaId)
            this.formSubmitLabel = 'Atualizar'
            this.$refs.inputNome.focus()
        },
        deletePerson(personId) {
            this.deletingPerson = true

            const options = {
                method: 'DELETE',
            }
            fetch(`/pessoas/${personId}`, options)
                .then(data => {
                    this.deletingPerson = false

                    if (!data.ok) {
                        throw new Error(data.status)
                    }

                    this.clearForm()
                    alert('Registro removido com sucesso', 'info')
                    this.getPersonData()
                })
                .catch(error => alert(error))
        },
    },
}).mount('#app')

$(function () {
    $('#rg').mask('00.000.000-0', { placeholder: '__.___.___.-_' });
    $('#cpf').mask('000.000.000-00', { placeholder: '___.___.___.-__' });
});