'use client';
import { useState } from 'react';

const Toggle = () => {
  const [isToggled, setIsToggled] = useState(false);

  const handleToggle = () => {
    setIsToggled(!isToggled);
  };

  return (
    <button
      className={`bg-white w-12 h-6 rounded-full focus:outline-none ${
        isToggled ? 'bg-black' : 'bg-white'
      }`}
      onClick={handleToggle}
    >
      <span
        className={`block w-5 h-5 m-0.5 rounded-full transform transition-transform ease-in-out ${
          isToggled ? 'translate-x-6' : ''
        } ${isToggled ? 'bg-white' : 'bg-black'}`}
      />
    </button>
  );
};

export default Toggle;
