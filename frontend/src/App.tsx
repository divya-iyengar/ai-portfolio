import "./App.css";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Projects from "./pages/Projects";
import Experience from "./pages/Experience";
import {Routes, Route } from "react-router-dom";
function App() {
  return (
    <div className="app">
      <Navbar />

      <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/experience" element={<Experience />} />
          <Route path="/projects" element={<Projects />} />
      </Routes>
    </div>
  );
}

export default App;