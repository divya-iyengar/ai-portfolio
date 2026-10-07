import ChatWindow from "./ChatWindow";
import "./AssistantSection.css"

function AssistantSection() {
    return (
        <section className="assistant-section">
            <h2>
                Ask Divya AI
            </h2>

            <p>
                Ask me about my experience, projects, research and technical background.
            </p>

            <ChatWindow />
        </section>
    );
}

export default AssistantSection;