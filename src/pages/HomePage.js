import React, {useState, useEffect, useContext} from 'react'
import AuthContext from '../context/AuthContext'
import useAxios from '../utils/useAxios'


const HomePage = () => {
  let [notes, setNotes] = useState([])
  let [harvest, setHarvest] = useState([])
  // let [userDetail, setUserDetail] = useState([])
  let {authTokens, logoutUser} = useContext(AuthContext)

  let api = useAxios()


  useEffect(()=> {
    getNotes()
    //deleteHarvest()
    //createUser()
    // getUserDetail()
  }, [])


  let getNotes = async() =>{
    let response = await api.get('/api/userList/')

    if(response.status === 200){
        setNotes(response.data)
    }
      
}
  
  //   let data = await response.json()

  //   if(response.status == 200) {
  //     setNotes(data)
  //   }
  //   else{
  //     logoutUser()
  //   }

  //   setNotes(data)
  //   console.log('DATA:', data)
  // }

  // let getUserDetail = async()=> {
  //   let response = await fetch('http://127.0.0.1:8000/api/userDetail/1', {
  //     method:'GET',
  //     headers:{
  //       'Content-Type':'application/json',
  //       'Authorization':'Bearer ' + String(authTokens.access)
  //     }
  //   })
  //   let data = await response.json()

  //   if(response.status == 200) {
  //     setUserDetail(data)
  //   }
  //   else{
  //     logoutUser()
  //   }

  //   setUserDetail(data)
  //   console.log('DATA:', data)
  // }


  // let deleteHarvest = async()=> {
  //   let response = await fetch('http://127.0.0.1:8000/api/harvestDelete/2', {
  //     method:'GET',
  //     headers:{
  //       'Content-Type':'application/json',
  //       'Authorization':'Bearer ' + String(authTokens.access),
  //     }
  //   })
    
  //   if(response.status == 200) {
  //     //alert('Deleted.!')
  //     console.log('Harvest Delete!')
  //   }
  //   else{
  //     logoutUser()
  //   }
  // }

  // let createUser = async()=> {
  //   let response = await fetch('http://127.0.0.1:8000/api/userCreate/', {
  //     method:'POST',
  //     headers:{
  //       'Content-Type':'application/json',
  //       'Authorization':'Bearer ' + String(authTokens.access),
  //     },
  //     body:JSON.stringify({'email':'volenecum01@gmail.com', 'password':'picare007', 'full_name':'Vole Necum01'})
  //   })
    
  //   if(response.status == 200) {
  //     //alert('Deleted.!')
  //     console.log('Harvest Delete!')
  //   }
  //   else{
  //     logoutUser()
  //   }
  // }

  

  return (
    <div>
        {/* <p>Jsi pripojen k home page</p>

    <h1>Uzivatele</h1>
    <ul>
        <li>{notes.full_name}</li>
    </ul> */}

    <h1>Uzivatel Detail</h1>
    <ul>
      {notes.map(note=> (
        <li key={note.id}>{note.full_name}</li>
      ))}
    </ul>

    </div>
  )
}

export default HomePage