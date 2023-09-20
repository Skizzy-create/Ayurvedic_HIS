import Image from 'next/image';
import React from 'react';
import MicIcon from '@mui/icons-material/Mic';

const Input = () => {
  return (
    <div>
      <div className="flex rounded-xl focus:border-blue-500 focus:outline-none  border bg-white ">
        <input
          type="text"
          placeholder="Typing Query..."
          className=" py-4 m:w-full  md:w-96 lg:w-182 pl-10  flex rounded-4xl"
        />
        <MicIcon className=" rounded-3xl m-auto   border-gray-300  w-12 h-12 pr-4 " />
      </div>
    </div>
  );
};

export default Input;
