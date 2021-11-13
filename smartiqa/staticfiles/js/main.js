const tags = document.getElementById("tags")
for(let i = 0; i < tags.childNodes.length; i++){
    let colors = ["is-primary", "is-danger", "is-success", "is-info", "is-link"]
    let rClass = colors[Math.round(Math.random() * colors.length)]
    if(i % 2 === 1){
        tags.childNodes[i].className = `button ${rClass} m-2`
    }
}