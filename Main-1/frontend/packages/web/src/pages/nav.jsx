import Chats from '../components/Chats'
export const Nav = () => {
  
  return (
    <nav className="flex justify-between p-4 font-poiret_one flex-col" style={{position: 'relative',}}>
      <div className="flex">
        <a href="/">
          <h1 className="text-4xl font-black text-white mr-5">
            Study Buddy
          </h1>
        </a>
      </div>
    </nav>
  );
};

export default Nav