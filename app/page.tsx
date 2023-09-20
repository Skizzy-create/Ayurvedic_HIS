import Image from 'next/image';
import Input from './components/Input';
import Navbar from './components/Navbar';
import Toggle from './components/toggle';
import Message from './components/Message';

export default function Home() {
  return (
    <main className="bg-backg min-h-screen flex ">
      <div>
        <Navbar />
      </div>
      <div className="bg-primary h-182 w-full  rounded-xl relative flex justify-center items-center m-4  ">
        <div className="flex absolute top-6 gap-x-2">
          <div>Eng</div>
          <div>
            <Toggle />
          </div>

          <div>हिन्दी</div>
        </div>
        <div className="absolute bottom-40 left-20  ">
          <Message />
        </div>
        <div className="absolute bottom-6  ">
          <Input />
        </div>
      </div>
    </main>
  );
}
