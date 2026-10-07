import "./Navbar.css";
import { Link } from "react-router-dom";

function Navbar() {
    return(
        <nav className="navbar">
            <Link to="/" className="navbar-brand">
                Divya Iyengar
            </Link>

            <div className="navbar-links">
                <Link to="/about">
                    About
                </Link>
                <Link to="/experience">
                    Experience
                </Link>
                <Link to="/projects">
                    Projects
                </Link>
                <Link to="/assistant">
                    AI Assistant
                </Link>
                <Link to="/resume.pdf">
                    Resume
                </Link>
            </div>
        </nav>
    );
}

export default Navbar;
