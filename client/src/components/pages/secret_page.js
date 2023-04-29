import React, { useState } from "react";

const Secret_page = () => {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
  };

  return (
    <div>
      <h1>ONLY AFTER LOGIN</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} accept=".pdf" />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
};

export default Secret_page;
