export interface Message {
    role:  string;
    content: string;
}

export interface ChatResponse {
    answer: string;
    sources: string[];
}