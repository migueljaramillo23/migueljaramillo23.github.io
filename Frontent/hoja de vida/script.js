function downloadPDF(){
    const element = document.querySelector("#pdf-content");

   /* console.log("si ingresoooo");
    console.log(element); */

    const hv ={
        margin: [10, 5, 15, 5], //[arriba, izquierdo, abajo, derecha] en mm 
        filename: "hoja_de_vida_miguel_Jaramillo_vallejo",
        image: { type: "jpeg", quality: 0.98},
        html2canvas:{
            scale: 2,
            useCORS:true,
            arrowTaint: false,
            scrollY: 0 

        },
        jsPDF: {
            unit: "mm",
            format: "a4",
            orientation: "portrait"

        }
    
    };
    html2pdf().set(hv).from(element).save();

    
}
