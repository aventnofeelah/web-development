const btn = document.getElementById("new-task-btn");
const tasks = document.getElementById("tasks");

btn.addEventListener("click", function(){
    let val = document.getElementById("new-task-input").value.trim();

    if(val === ""){return;}

    const task = document.createElement('div');
    const check = document.createElement('input');
    const label = document.createElement('label');
    const del = document.createElement("button");

    del.addEventListener("click", function(){
        task.remove();
    })
    check.type = 'checkbox';
    task.className = "task";
    label.textContent = " " + val;

    tasks.appendChild(task);
    task.appendChild(check);
    task.appendChild(label);
    task.appendChild(del);

    check.addEventListener("click", function(){
        label.style.textDecoration = "line-through";
    })

})


