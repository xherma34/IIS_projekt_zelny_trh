import React, {useContext} from 'react'
import { Link } from 'react-router-dom'
import AuthContext from '../context/AuthContext'

const Footer = () => {
    let {user, logoutUser} = useContext(AuthContext)
    return (
        <div>
            <Link to="/" >Home</Link>
            <span> | </span>
            {user ? (
                <p onClick={logoutUser}>Logout</p>
            ): (
                <Link to="/login" >Login</Link>
            )}
            <span> | </span>
            <Link to="/register" >Register</Link>
            {user && <p>Hello {user.full_name}</p>}
            <span> | </span>
            <Link to="/catalog" >Catalog</Link>
            <span> | </span>
            <Link to="/crop" >Crops</Link>
            <span> | </span>
            <Link to="/admin">AdminPage</Link>
            <span> | </span>
            <Link to="/userinfo">UserInfo</Link>
            <span> | </span>
            <Link to="/suggestion">SuggestionPage</Link>
        </div>
  )
}

export default Footer