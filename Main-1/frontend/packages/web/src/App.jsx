import "./App.css";
import { Mike } from "./components/mike";
import Nav from './pages/nav'
import StoryCard from "./components/storyCard";
import Chats from './components/Chats'
import OutputContainer from "./components/OutputContainer";
import NewContainer from './components/NewContainer'
import { useState } from "react";

function App() {
  const [output,setOutput]=useState('')
  return (
      <>
      <NewContainer onOpChange={setOutput}/>
      <OutputContainer otpt={output} />
      </>
  );
}

export default App;

{/* <StoryCard
              key={story.id}
              id={story.id}
              heading={story.title}
              imgSrc={`${story.img}`.replaceAll("*","")}
              content={story.story}
            ></StoryCard> */}