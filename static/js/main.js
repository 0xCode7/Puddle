const passwordField = document.getElementById('password')
const toggleBtn = document.getElementById('toggleBtn')
const eye = document.getElementById('eye')
toggleBtn.addEventListener('click', () => {
    console.log('clicked')
    if (passwordField.type === 'password') {
        passwordField.type = 'text'
        eye.style.color = '#428bfc'
    } else {
        passwordField.type = 'password'
        eye.style.color = 'gray'

    }
})