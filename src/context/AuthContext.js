import { createContext, useState, useEffect } from "react";
import jwt_decode from "jwt-decode";
import { useHistory} from 'react-router-dom'

const AuthContext = createContext()

export default AuthContext;

export const AuthProvider = ({children}) => {
    
    //localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null

    let [authTokens, setAuthTokens] = useState(()=> localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null)
    let [user, setUser] = useState(()=> localStorage.getItem('authTokens') ? jwt_decode(localStorage.getItem('authTokens')) : null)
    let [loading, setLoading] = useState(true)

    const history = useHistory()

    let loginUser = async (e ) => {
        e.preventDefault()
        // console.log('Form submitted')
        let response = await fetch('http://127.0.0.1:8000/api/token/', {
            method:'POST',
            headers:{
                'Content-Type':'application/json',
            },
            body:JSON.stringify({'email':e.target.email.value, 'password':e.target.password.value})
        })
        let data = await response.json()
        // console.log('data:', data)
        // console.log('response:', response)

        if(response.status == 200) {
            setAuthTokens(data)
            setUser(jwt_decode(data.access))
            localStorage.setItem('authTokens', JSON.stringify(data))
            history.push('/')
        }
        else {
            console.log('WentWrong',response.status)
            alert('Went wrong!')
        }
    }

    // let registerUser = async (e ) => {
    //     e.preventDefault()
    //     // console.log('Form submitted')
    //     let response = await fetch('http://127.0.0.1:8000/api/createUser/', {
    //         method:'POST',
    //         headers:{
    //             'Content-Type':'application/json',
    //         },
    //         body:JSON.stringify({'email':e.target.email.value, 'password':e.target.password.value, 'full_name':e.target.full_name})
    //     })
    //     let data = await response.json()
    //      console.log('data:', data)
    //      console.log('response:', response)

    //     // if(response.status == 200) {
    //     //     setAuthTokens(data)
    //     //     setUser(jwt_decode(data.access))
    //     //     localStorage.setItem('authTokens', JSON.stringify(data))
    //     //     history.push('/')
    //     // }
    //     // else {
    //     //     console.log('WentWrong',response.status)
    //     //     alert('Went wrong!')
    //     // }
    // }


    let logoutUser = () => {
        setAuthTokens(null)
        setUser(null)
        localStorage.removeItem('authTokens')
        history.push('/login')
    }


    // let updateToken = async ()=> {
    //     console.log('update was called')
    //     let response = await fetch('http://127.0.0.1:8000/api/token/refresh/', {
    //         method:'POST',
    //         headers:{
    //             'Content-Type':'application/json'
    //         },
    //         body:JSON.stringify({'refresh':authTokens?.refresh})
    //     })
    //     let data = await response.json()

    //     if(response.status == 200)
    //     {
    //         setAuthTokens(data)
    //         setUser(jwt_decode(data.access))
    //         localStorage.setItem('authTokens', JSON.stringify(data))
    //     }
    //     else {
    //         logoutUser()
    //     }

    //     if(loading) {
    //         setLoading(false)
    //     }

    // }


    let contextData = {
        user:user,
        authTokens:authTokens,
        setAuthTokens:setAuthTokens,
        setUser:setUser,
        loginUser:loginUser,
        logoutUser:logoutUser
    }
    

    useEffect(()=> {

        if(authTokens){
            setUser(jwt_decode(authTokens.access))
        }
        setLoading(false)
 
    }, [authTokens, loading])


    return(
        <AuthContext.Provider value={contextData} >
            {loading ? null : children}
        </AuthContext.Provider>
    )
}
