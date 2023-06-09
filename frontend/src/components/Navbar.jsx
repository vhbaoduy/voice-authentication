import { Link, useMatch, useResolvedPath } from "react-router-dom"
import React from "react"

import "../styles/Navbar.css"

function Navbar() {
  return (
    <nav className="nav">
      <Link className="site-title" to="/">
          <ul>
          Voice Authentication
          </ul>
      </Link>
      <ul>
        <CustomLink to="/">Home</CustomLink>
        <CustomLink to="/setting">Setting</CustomLink>
        {/* <CustomLink to="/about">About</CustomLink> */}
      </ul>
    </nav>
  )
}

function CustomLink({ to, children, ...props }) {
  const resolvedPath = useResolvedPath(to)
  const isActive = useMatch({ path: resolvedPath.pathname, end: true })

  return (
    <li className={isActive ? "active" : ""}>
      <Link to={to} {...props}>
        {children}
      </Link>
    </li>
  )
}

export default Navbar