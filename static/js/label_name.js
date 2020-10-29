function setFileName(id){
    valor=document.getElementById(id).value
    valor=valor.split("\\")
    if(valor!=""){
        name=document.getElementById((id+"-label")).textContent=valor[valor.length-1]
    }
}