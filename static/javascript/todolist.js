let todolist = document.querySelector('.list')
let inputField = document.querySelector('#add-reminder')

function addToList() {
    let text = inputField.value
    inputField.value = ''

    if (text) {
    
        let reminderDiv = document.createElement('div')
        reminderDiv.classList.add('reminder-wrapper')

        let newReminder = document.createElement('LI')
        newReminder.innerHTML = text
        newReminder.classList.add('list-element')

        let complete = document.createElement('button')
        complete.innerHTML = '⚪️'
        complete.classList.add('complete')
        complete.onclick = function () {
            if (complete.innerHTML.includes('⚪️')) {
                complete.innerHTML = '🔘'
                newReminder.style.opacity = '0.2'
            } else {
                complete.innerHTML = '⚪️'
                newReminder.style.opacity = '1'
            }
        }

        let deleteLi = document.createElement('button')
        deleteLi.innerHTML = '❌'
        deleteLi.classList.add('delete')
        deleteLi.onclick = function () {
            deleteLi.parentElement.parentElement.removeChild(reminderDiv)
        }

        reminderDiv.appendChild(complete)
        reminderDiv.appendChild(newReminder)
        reminderDiv.appendChild(deleteLi)

        todolist.appendChild(reminderDiv)
    }
}