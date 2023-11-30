import { useState } from "react";

export default function NewContainer(props) {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const getKeyWords = async () =>{
    const response = await fetch('http://127.0.0.1:5001/get_summary');
    const kw = await response.json();
    props.onOpChange(kw.result)
    return kw;
  }

  const handleUpload = () => {
      fetch('http://localhost:3000/upload', {
        method: 'POST',
        body: '1',
      })
        .then(response => response.text())
        .then(message => {
          alert(message);
        })
        .catch(error => {
          console.error('Error:', error);
        });
  };

  return (
    <div className="new-container">
        {/* <input type="file" onChange={handleFileChange} /> */}
        <button onClick={handleUpload}>Upload</button>
        <button onClick={getKeyWords}>Generate Summary</button>
    </div>
    );
    
}