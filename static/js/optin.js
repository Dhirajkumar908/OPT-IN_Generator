function captureTable(tableid,imgname) {
    const table = document.getElementById(tableid);
    html2canvas(table).then(function(canvas) {
        const imgData = canvas.toDataURL('image/png');

        // // You can display the image, save it, or send it to the server
        // const img = new Image();
        // img.src = imgData;
        // document.body.appendChild(img);
        // Create a link to download the image
        const a = document.createElement('a');
        a.href = imgData;
        a.download = imgname+'.jpeg'; // Specify the desired file name and extension

        // Trigger a click event on the link to download the image
        a.click();

        // If you want to save it as a PDF, you can send the image data to the server and convert it to PDF using a Python library.
    });
    
}


// function captureTable(tableid, imgname){
//     const element=document.getElementById(tableid);
//     element.remove();
// }

function captureTable(tableid,imgname) {
    const table = document.getElementById(tableid);
    html2canvas(table).then(function(canvas) {
        const imgData = canvas.toDataURL('image/png');
        const a = document.createElement('a');
        a.href = imgData;
        a.download = imgname+'.jpeg'; // Specify the desired file name and extension
        a.click();
    });
}

function captureAllTables() {
    const divIds = ['div1', 'div2', 'div3']; // Update this array with IDs of all your div sections
    const zip = new JSZip();

    divIds.forEach(function(divId) {
        const div = document.getElementById(divId);
        html2canvas(div).then(function(canvas) {
            const imgData = canvas.toDataURL('image/png');
            const imgName = divId + '.png'; // Use div ID as image name
            zip.file(imgName, imgData.split(',')[1], {base64: true});
        });
    });
}