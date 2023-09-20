import React from 'react';
import AccessibilityNewOutlinedIcon from '@mui/icons-material/AccessibilityNewOutlined';
import PersonIcon from '@mui/icons-material/Person';
const Navbar = () => {
  const iconStyle = {
    fontSize: '2rem',
    margin: '10px ', // You can adjust the size by changing the value
  };
  return (
    <div className="bg-[#404241] rounded-r-3xl h-full flex-col py-8 space-y-4 px-2">
      <div className="bg-white 	 rounded-3xl ">
        <AccessibilityNewOutlinedIcon style={iconStyle} />
      </div>
      <div className="bg-white rounded-3xl">
        <PersonIcon style={iconStyle} />
      </div>
    </div>
  );
};

export default Navbar;
