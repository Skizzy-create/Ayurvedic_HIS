import { Badge } from '@/components/ui/badge';
import React from 'react';

const page = () => {
  return (
    <div className="bg-[#404241] h-screen p-10 ">
      <h1 className="text-4xl text-primary  ">Profile Dashboard</h1>

      <div className="flex gap-x-4 p-8 justify-center items-center">
        <Badge className="p-2 bg-[#F1ECE9F2]">prakirti state</Badge>
        <Badge className="p-2">Stats</Badge>
        <Badge className="p-2">settings</Badge>
      </div>
      <div className="w-4/6 m-auto justify-center items-center bg-[#505E570F] h-full py-4 px-40 ">
        <h1 className="text-5xl bold m-6 text-center "> Kapha State</h1>
        <p className="text-center text-xl leading-normal	 ">
          Kapha is associated with the elements of water and earth. It governs
          stability, structure, and lubrication in the body. People with a
          balanced Kapha dosha tend to be calm, patient, and have strong
          immunity. An excess of Kapha can lead to lethargy, weight gain, and
          respiratory issues.
        </p>
      </div>
    </div>
  );
};

export default page;
