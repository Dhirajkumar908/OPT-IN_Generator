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
        a.download = imgname+'.png'; // Specify the desired file name and extension

        // Trigger a click event on the link to download the image
        a.click();

        // If you want to save it as a PDF, you can send the image data to the server and convert it to PDF using a Python library.
    });
}


