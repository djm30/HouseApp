updateRotaBtn = document.querySelector("#updateRotaBtn")
updateRotaCheckboxes = document.querySelectorAll(".updateRotaCheckboxes")



let rotaButtonInfo = {
    updating: false
}




let showCheckboxes = function(){
    $( " .updateRotaCheckboxes" ).show()
    $( " #taskModalBtn" ).hide()
}

let hideCheckboxes = function(){
    $( " .updateRotaCheckboxes" ).hide()
    $( " #taskModalBtn" ).show()
    for(let check of updateRotaCheckboxes){
        check.checked = false
    }
}

let makeButtonGreen = function(){
    updateRotaBtn.classList.remove("btn-primary")
    updateRotaBtn.classList.add("btn-success")
}

let makeButtonBlue = function(){
    updateRotaBtn.classList.remove("btn-success")
    updateRotaBtn.classList.add("btn-primary")
}


let updatePressed = function(button){
    button.innerHTML = "Confirm Update"
    // showCheckboxes()
    showCheckboxes()
    makeButtonGreen()

}

function updateDiv()
{ 	
    hideCheckboxes();
}

hideCheckboxes()



let confirmUpdate = function(button){
    let tasksToUpdate = {
        selected : []
    }
    for(let check of updateRotaCheckboxes){
        if(check.checked){
            tasksToUpdate.selected.push(check.id)
        }
    }
    button.innerHTML = "Update"
    makeButtonBlue()
    hideCheckboxes()

    //Send data to flask i guess
    
    axios.patch("/tasks/update", tasksToUpdate)
    .then((response) =>{
        console.log(tasksToUpdate) 
        location.reload()

    })
    .catch((error) =>{
        console.log(error)
    })

}




updateRotaBtn.addEventListener("click", function(event) {
    if(!rotaButtonInfo.updating) {
        updatePressed(this)
    }
    else{
        console.log(confirmUpdate(this))
    }
    rotaButtonInfo.updating = !rotaButtonInfo.updating
})



addTaskFormBtn = document.querySelector("#taskFormBtn")
taskNameInput = document.querySelector("#taskNameInput")
startingUserInput = document.querySelector("#startingUserInput")

addTaskFormBtn.addEventListener("click", function(event) {
    event.preventDefault()
    console.log()
    console.log(startingUserInput.value)

    taskToAdd = {
        task_name : taskNameInput.value,
        current_user : parseInt(startingUserInput.value)
    }
    console.log(taskToAdd)
    axios.post("/tasks/add", taskToAdd)
    .then((response) =>{
        console.log(response)
        location.reload()

    })
    .catch((error) =>{
        console.log(error)
    })

})
