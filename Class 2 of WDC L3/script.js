let addw=document.getElementById("add");
let shoppinglist=document.getElementById("shopping-list");
let todolist=[];
window.onload=()=>{
  todolist=JSON.parse(localStorage.getItem("todo_list"))||[];
  todolist.forEach(argument1=>add_tasks_todo(argument1));
}

function render_data(){
    let datas="";
    todolist.forEach((task)=>{
        let html=`
     <li class="list-group-item d-flex justify-content-between lh-sm ">
            <h5 class="my-0 lll">${task}</h5></li>`
    datas=datas+html;
    })
    shoppinglist.innerHTML=datas;
    let li_count=todolist.length;
  document.getElementById("cart_counter").innerHTML=li_count;
  strike();
  delete_task();
  localStorage.setItem("todo_list",JSON.stringify(todolist));
}
render_data()

function add_task(){
    if (addw.value!=""){
        todolist.push(addw.value);
        addw.value="";
    }
    render_data();
}

function strike(){
    let list_items=document.querySelectorAll(".lll");
    list_items.forEach((task)=>{
        task.addEventListener("click",()=>{
            task.style.textDecoration="line-through";
        })
    })
}

// function delete_task(){
//     let list_items=document.querySelectorAll(".lll");
//     list_items.forEach((task,index)=>{
//         task.addEventListener("dblclick",()=>{
//            todolist.splice(index,1);
//         })
//     })
//     render_data();
// }
function delete_task() {
    let list_items = document.querySelectorAll(".lll");
    list_items.forEach((task, index) => {
      task.addEventListener("dblclick", () => {
        todolist.splice(index, 1);
        render_data(); // Call render_data to update the list after deletion
      });
    });
  }










// function atsl(){
//   var li=document.createElement("li");
//   li.innerHTML=`
//     <li  class="list-group-item d-flex justify-content-between lh-sm">
//             <h5 class="my-0">${addw.value}</h5> <a onclick="del(event)" class="btn btn-primary btn-sm">Delete</a>
//         </li>
//     `
//   shoppinglist.appendChild(li);
//   // var li_count=document.querySelectorAll("li").length;
//   cart_counter=cart_counter+1;
//   document.getElementById("cart_counter").innerHTML=cart_counter;
// }

// function del(event){
//   event.target.parentElement.parentElement.remove();
//   cart_counter=cart_counter-1;
//   document.getElementById("cart_counter").innerHTML=cart_counter;
// }

