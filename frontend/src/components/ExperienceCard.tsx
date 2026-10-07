import RoleCard from "./RoleCard";

interface RoleData {
    role: string
    duration: string
    summary: string
    contributions: string[]
}

type ExperienceCardProps = {
    company: string;
    duration: string;
    roles: RoleData[]
};

function ExperienceCard({
    company,
    duration,
    roles
}: ExperienceCardProps) {
    return (
        <div className="experience-card">
            <h2>{company}</h2>
            <p>{duration}</p>
            <ul>
                {roles.map((item, index) => (
                    <RoleCard key={index} {...item} />
                ))}
            </ul>
        </div>
    );
}

export default ExperienceCard;