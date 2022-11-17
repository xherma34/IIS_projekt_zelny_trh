import React, {useContext} from 'react'
import AuthContext from '../context/AuthContext'

const LoginPage = () => {
    let {loginUser} = useContext(AuthContext)
    return (
    <div>
        <form onSubmit={loginUser}>
            <input type="text" name="email" placeholder='Your email:' />
            <input type="password" name="password" placeholder='Your password:' />
            <input type="submit" />
        </form>
    </div>
  )
}

export default LoginPage