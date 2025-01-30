import React from 'react';
import ProductCard from './ProductCard';
import images from "./assets/images.png";
const RightPanel = ({ imageurl }) => {
  return (
    <div style={{
      overflow: 'auto',
      scrollbarWidth: 'none', /* Firefox */
      msOverflowStyle: 'none', /* IE and Edge */
    }} className="flex flex-col items-center p-4 w-full h-full rounded-lg shadow-md bg-gradient-to-b from-[#004AAD] to-[#5DE0E6]">
      {/* <div className="flex flex-col w-full md:w-1/4"> */}
      <ProductCard
        title="Designed by Sanat Chaudhary"
        description="Upload the pdf and ask anything about it ..."
        image={images}  // Replace with the actual image path
        price="₹2000"
      />
      <br/>
      <br/>
      <h1 className="text-lg font-bold text-gray-800 mb-2">{imageurl}</h1>

      {/* </div> */}
    </div>
  );
};

export default RightPanel;
