import ReactMarkdown from 'react-markdown';
export default function OutputContainer(props){
    return (
        <div className="output-container">
            <ReactMarkdown style={{ whiteSpace: 'pre-line' }}>
                {props.otpt}
            </ReactMarkdown>
        </div>
    )
}