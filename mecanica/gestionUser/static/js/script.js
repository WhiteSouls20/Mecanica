const color = 'blue'

let btnInicio = document.getElementById('inicio')



btnInicio.addEventListener("mouseover", function() {
    // btnInicio.style = "font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; color: blue; font-size: 30px; font-weight: bold; margin-top: 25px;"
    this.style.color = '#38b6ff';
})

btnInicio.addEventListener("mouseout", function() {
    // btnInicio.style = "font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; color: white; font-size: 30px; font-weight: bold; margin-top: 25px;"
    this.style.color = 'white';
})

btnInicio.addEventListener("mouseout", function () {
    // this.style.transform = 'scale(1)';
     this.style.transition = '1s';
})

