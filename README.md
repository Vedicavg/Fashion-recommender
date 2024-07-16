*** main.py file  
-> This file runs the streamlit application for recommendation system
    To run the file ` streamlit run main.py `
    This runs the server at ` http://localhost:8501 `

*** main1.py file 
->This file is an api that returns an array of images similar to the image sent to it

-> To get the array make a post request to the following url :
    ` http://localhost:5000/process_image `

->key for sending the image is `image`

-> Example code ( if you are using nodejs and axios ) :
`  app.post("/upload",upload.single("file") ,async (req,res)=> `   
`{    `
`
`    
`    let imgpath = path.join(__dirname,req.file.path); `
`    const formData = new FormData(); `
`    formData.append("image",fs.createReadStream(imgpath));// the key to send is image for the api `
`    `
`    try {  `
`        const response = await axios.post(apiUrl,formData, { `
`            headers:{ `
`                ...formData.getHeaders(), `
`                
`            } `
`            
`        }); `
` `
`    } catch (error) { `
`        console.error(error); `
`        res.status(500).send("Error uploading file"); `
`    } `
`      `
` }); ` 

 The returned object would be like this :
 `  {
    similar_images: [
      'fashion_small/images/8892.jpg',
      'fashion_small/images/10260.jpg',
      'fashion_small/images/15612.jpg',
      'fashion_small/images/9164.jpg',
      'fashion_small/images/9178.jpg'
    ]
  } `
