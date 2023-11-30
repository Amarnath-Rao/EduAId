import { useNavigate } from "react-router-dom";

const ChatComp = ({ heading, content, imgSrc, id }) => {

  const navigate = useNavigate();

  const handleClick = () => {
    navigate("/story/" + id);
  }

  return (
    <div onClick={handleClick} style={{padding: '10px',paddingLeft: '20px',}}>{heading}</div>
  )
}
export default ChatComp