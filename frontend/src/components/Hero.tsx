import "./Hero.css"

function Hero() {
    return (
        <section className="hero">
            <div className="hero-content">
                <h1>
                    Divya Iyengar
                </h1>
                <h2>
                    Applied AI Engineer
                </h2>
                <p>
                    Building intelligent systems spanning robotics, autonomous driving, and generative AI applications.
                </p>

                <div className="hero-links">
                    <a 
                    href="/resume.pdf"
                    target="_blank"
                    >
                    Resume
                    </a>

                    <a 
                    href="https://github.com/divya-iyengar"
                    target="_blank"
                    rel="noopener noreferrer"
                    >
                    GitHub
                    </a>

                    <a 
                    href="https://www.linkedin.com/in/divya-iyengar-0a4011171"
                    target="_blank"
                    rel="noopener noreferrer"
                    >
                    LinkedIn
                    </a>
                </div>
            </div>

            <div className="hero-image">
                <img
                    src="/profile.jpg"
                    alt="Divya Iyengar"
                />
            </div>
        </section>
    );
}

export default Hero;