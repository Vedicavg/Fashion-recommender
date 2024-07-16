# Fashion Recommendation System
-To download the dependencies run  
      ` pip install -r requirements.txt `  
-First run the ` test.py ` using :  
      ` python test.py `

## Overview

### main.py

This file runs the Streamlit application for the recommendation system.

To run the application locally:

```bash
streamlit run main.py
```
##main1.py
This file serves as an API that returns an array of images similar to the image sent to it.

Endpoint:
``` POST /process_image ```
Request Body:
Key: 'image'
Description: The image file to be processed.  
```
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');
const path = require('path');

const apiUrl = 'http://localhost:5000/process_image';

app.post('/upload', upload.single('file'), async (req, res) => {
  let imgpath = path.join(__dirname, req.file.path);
  const formData = new FormData();
  formData.append('image', fs.createReadStream(imgpath));

  try {
    const response = await axios.post(apiUrl, formData, {
      headers: {
        ...formData.getHeaders(),
      },
    });

    // Handle response
    console.log(response.data);
    res.status(200).json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).send('Error uploading file');
  }
});
```
### Response Format:
Upon successful request, the API responds with an object containing an array of similar image paths:  

```
{
  "similar_images": [
    "fashion_small/images/8892.jpg",
    "fashion_small/images/10260.jpg",
    "fashion_small/images/15612.jpg",
    "fashion_small/images/9164.jpg",
    "fashion_small/images/9178.jpg"
  ]
}
```


