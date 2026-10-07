import { useState } from "react";

interface Props {
    onSend: (message: string) => void;
}

function InputBox({onSend}: Props) {
    const [input, setInput] = useState("");

    function handleSend() {
        onSend(input);
        setInput("");
    }
    return(
        <div className="chat-input">
            <input 
            value ={input}
            onChange={(event) => setInput(event.target.value)}
            onKeyDown={(event) => {
                if (event.key == "Enter") {
                    handleSend();
                }
            }}
            placeholder="Type a question..."
            />
            <button onClick={handleSend}>
            Send
            </button>
        </div>
    );
}

export default InputBox;