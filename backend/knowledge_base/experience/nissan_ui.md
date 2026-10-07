# Nissan Advanced Technology Center

## Role
AI Research Engineer
October 2024 - March 2025

## Summary

As an AI Research Engineer, I developed proof-of-concept AI experiences exploring how generative AI could create personalized, context-aware interactions for vehicle occupants. My work focused on transforming real-time vehicle and driver sensor data into engaging in-cabin experiences by combining software engineering, Unity visualizations, large language models, and vehicle integrations.

Rather than building foundation models, I deigned the application layer that orchestrated sensor inputs, backend AI reasoning, and interactive vehicle responses to demonstrate future human-vehicle interaction concepts. 

## Key Contributions

### Context-Aware In-Vehicle AI Experiences

Developed interactive demonstrations that adapted vehicle behavior based on real-time contextual information, including driver state and environmental sensor inputs.

Experiences included:
- Personalized avatar greetings upon vehicle entry
- Dynamic mood-setting through coordinated lighting and music selection
- Location-aware promotional experiences triggered by nearby points of interest
- AI-generated conversational interactions tailored to the current driving context

### LLM-Orchestrated Decision Making

Designed backend workflows that transformed structured vehicle and driver context into prompts for a Large Language Model.

The application supplied the LLM with:
- current driver state
- relevant sensor information
- Context surrounding experience being presented (i.e., restaurant promotion)
- Desired interaction objectives

Rather than generating arbitrary responses, the LLM determined *how* the interaction should be delivered, including decisions such as whether the avatar should respond verbally or non-verbally, ask a brief engaging question, or provide a more detailed explanation.

### End-to-End AI Application Integration

Integrated multiple software components into a cohesive AI application pipeline.

The overall workflow included:
- Processing cleaned sensor inputs
- Triggering contextual application events
- Calling backend LLM services
- Interpreting model responses
- Coordinating avatar behaviors
- Updating Unity-based user interfaces
- Integrating third-party services such as the Spotify API for personalized media experiences

### Local LLM Client-Server Integration

Developed the user-side integration for a local client-server architecture that enabled communication with a DeepSeek model hosted on an onboard NVIDIA server. 

Responsibilities included:
- Constructing HTTP REST requests to an OpenAI-compatible inference API
- Packaging prompts and model parameters as structured JSON payloads
- Parsing structured JSON responses returned by the model
- Handling request status and connection errors
- Decoupling frontend application logic from backend AI inference

This architecture enabled real-time interaction with a locally deployed language model while keeping compute-intensive inference isolated from the user application. 

### Human-Centered AI Interaction Design

Explored how conversational AI could create natural and engaging in-vehicle experiences by balancing contextual awareness, personalization, and user attention.

Iterated on prompt design and interaction flows to improve the relevance and tone of AI-generated responses while ensuring the resulting demonstrations remained intuitive and engaging.

## Technologies

Programming Languages
- Python
- C#

AI & Machine Learning
- Large Language Models (LLMs)
- Prompt Engineering
- Context-Aware AI Applications

Development
- Unity
- Spotify API
- REST APIs
- Backend AI services

## Challenges

A key challenge was designing AI interactions that felt natural rather than intrusive. Because responses depended on changing environmental conditions, driver state, and contextual events, prompt design and application logic needed to balance personalization with concise appropriate communication.

Another challenge involved coordinating multiple software components, including sensor processing, backend AI services, Unity visualizations, avatar behaviors, and external APIs, into a seamless real-time user experience.

## Lessons Learned 

This work demonstrated that building successful AI products requires far more than integrating a language model. Creating compelling user experiences depends on thoughtfully orchestrating data pipelines, prompt design, application logic, frontend interactions, and external services into a cohesive system.

This experience also strengthened my understanding of context-aware AI applications, reinforcing that the quality of an AI system often depends as much on the surrounding software architectuer and user experience as on the underlying model itself. 