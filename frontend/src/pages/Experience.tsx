import ExperienceCard from "../components/ExperienceCard";

function Experience() {
    return(
        <main className="experience-page">
            <h1>
                Experience
            </h1>

            <ExperienceCard
                company="Nissan Advanced Technology Center"
                duration="Oct 2024 - Present"
                roles={[
                    {
                        role: "Autonomous Driving Planner Research",
                        duration: "Apr 2025 - Present",
                        summary: "Developing intelligent planning software for autonomous driving, focusing on motion planning, AI-assisted decision making, and real-time robotics software.",
                        contributions: [
                            "Contribution 1.",
                            "Contribution 2."
                        ]
                    },
                    {
                        role: "AI Research Engineer",
                        duration: "Oct 2024 - Mar 2025",
                        summary: "Built AI-driven prototypes exploring intelligent interaction systems, machine learning workflows, and applied generative AI for future mobility applications.",
                        contributions: [
                            "Contribution 3.",
                            "Contribution 4."
                        ]
                    }
                ]}
            />

            <ExperienceCard
                company="Georgia Tech DART Lab"
                duration="Aug 2022 - Jan 2024"
                roles={[
                    {
                        role: "Graduate Research Assistant",
                        duration: "Hello",
                        summary: "Hello",
                        contributions: ["Hello"]
                    }
                ]}
            />
        </main>
    );
}

export default Experience;