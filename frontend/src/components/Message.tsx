import type { Message as ChatMessage } from "../types/chat";

interface Props {
    message: ChatMessage;
}
export function Message({ message }: Props) {
    return(
        <div className="message">
            <strong>{message.role}:</strong>
            <p>{message.content}</p>
        </div>
    );
}

export default Message;