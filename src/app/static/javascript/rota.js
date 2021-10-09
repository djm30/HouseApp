updateRotaBtn = document.querySelector("#updateRotaBtn")
updateRotaCheckboxes = document.querySelectorAll(".updateRotaCheckboxes")

let showCheckboxes = function(){
    for(let check of updateRotaCheckboxes){
        check.classList.remove("display-hide")
        check.classList.add("display-show")
    }
}

let hideCheckboxes = function(){
    for(let check of updateRotaCheckboxes){
        check.classList.remove("display-show")
        check.classList.add("display-hide")
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

hideCheckboxes()


let updatePressed = function(button){
    button.innerHTML = "Confirm Update"
    makeButtonGreen()
    showCheckboxes()

}

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
    
    axios.post("/tasks/update", tasksToUpdate)
    .then((response) =>{
        console.log(tasksToUpdate)
    })
    .catch((error) =>{
        console.log(error)
    })
}

let rotaButtonInfo = {
    updating: false
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