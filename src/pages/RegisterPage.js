import React, {useContext} from 'react'
import AuthContext from '../context/AuthContext'

const RegisterPage = () => {
    let {registerUser} = useContext(AuthContext)

    return (
    <div>
        <h1>Register</h1>
        <form onSubmit={registerUser}>
            <input type="text" name="email" placeholder='Your email:' />
            <input type="text" name="full_name" placeholder='Your full_name:' />
            <input type="password" name="password" placeholder='Your password:' />
            <input type="submit" />
        </form>
    </div>
  )
}

export default RegisterPage