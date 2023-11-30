import { useLayoutEffect, useState } from "react";
import ChatComp from "./chatComp";
import { fetchStories } from "../services/stories";
import '../App.css'
export default function Chats() {
  const [stories, setStories] = useState([]);

  useLayoutEffect(() => {
    fetchStories().then((res) => {
      setStories(res.stories);
    });
  }, []);

 

  return (
    <div className="chat-container">
      {stories?.map((story) => (
        <ChatComp heading={story.title} key={story.id} id={story.id}></ChatComp>
      ))}
    </div>
  );
}
