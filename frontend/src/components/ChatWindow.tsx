import { useState, useEffect, useRef } from "react";
import Message from "./Message";
import InputBox from "./InputBox";
import { Message as ChatMessage } from "../types/chat";
import { sendMessage } from "../services/api";

function ChatWindow() {
    const [messages, setMessages] = useState<ChatMessage[]>([
        {
        role: "assistant",
        content: "Hello! Ask me about Divya..."
        }
    ]);

    const hasUserInteracted = useRef(false);

    const messagesEndRef = useRef<HTMLDivElement | null>(null);

    async function handleSend(messageText: string) {

        hasUserInteracted.current = true;

        const userMessage: ChatMessage = {
            role: "user",
            content: messageText
        };

        setMessages(prev => [
            ...prev,
            userMessage
        ]);

        try {
            const response = await sendMessage(messageText);
            const assistantMessage = {
                role: "assistant",
                content: response.answer
            };

            setMessages(prev => [
                ...prev,
                assistantMessage
            ]);
        } catch (error) {
            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    content: "Sorry, I ran into an error."
                }
            ]);
        }
    }

    useEffect(() => {

        if (hasUserInteracted.current) {
            messagesEndRef.current?.scrollIntoView({
            behavior: "smooth"
            });
        }
    }, [messages]);

    return (
        <section className="chat-window">

            <div className="messages">
                {messages.map((msg, index)  => (
                    <Message key={index} message={msg}/>
                ))}
                <div ref={messagesEndRef} />
            </div>

            <InputBox onSend={handleSend}/>

        </section>
    );
}

export default ChatWindow;