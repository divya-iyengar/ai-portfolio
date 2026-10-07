
type RoleCardProps = {
    role: string
    duration: string
    summary: string
    contributions: string[]
};

function RoleCard({
    role,
    duration,
    summary,
    contributions
}: RoleCardProps) {
    return (
        <div className="role-card">
            <h3>{role}</h3>
            <p>{duration}</p>
            <p>{summary}</p>
            <ul>
                {contributions.map((item, index) => (
                    <li key={index}>
                        {item}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default RoleCard;