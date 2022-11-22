import React, {useState, useEffect, useContext} from 'react'
import useAxios from '../utils/useAxios'
import './AdminChangeUser.css'

const AdminChangeUser = ( {match} ) => {

	let[user, setUser] = useState([])
	let[firstName, setFirstName] = useState([])
	let[lastName, setLastName] = useState([])
	let[email, setemail] = useState([])
	let[phone, setphone] = useState([])
	let[dateob, setdateob] = useState([])
	let[bankAcc, setbankAcc] = useState([])

	useEffect(() => {
		getUser()
		
	}, [])

	let api = useAxios()

	let getUser = async() =>{
		let response = await api.get('/api/userDetail/'+match.params.id)

		if(response.status === 200)
		{
			setUser(response.data)
		}
		setFirstName(response.data.firstName)
		setLastName(response.data.lastName)
		setemail(response.data.email)
		setphone(response.data.phone)
		//setbankAcc(response.data.bankAccount)
		setdateob(response.data.dateOfBirth)
	}

	const changeFName = (event) =>{
		setFirstName(event.target.value)
		console.log("tady", firstName)
	}

	const changeLName = (event) =>{
		setLastName(event.target.value)
		console.log("tady", lastName)
	}

	const changeMail = (event) =>{
		setemail(event.target.value)
		console.log("tady", email)
	}

	const changePhone = (event) =>{
		setphone(event.target.value)
		console.log("tady", phone)
	}

	const changeBAcc = (event) =>{
		setbankAcc(event.target.value)
		console.log("tady", bankAcc)
	}

	const changeDOB = (event) =>{
		setdateob(event.target.value)
		console.log("tady", dateob)
	}

	let changeUser = async() =>{
		let response = await fetch('http://127.0.0.1:8000/api/userUpdate/'+match.params.id,{
			method:'POST',
			headers:{
				'Content-Type':'application/json',
			},
			body:JSON.stringify({"firstName":firstName, "lastName":lastName, "email":email, "dateOfBirth":dateob, "phone":phone})
		})
	}

	return (
		<div className='contentACU'>
			<div className='imgACU'>
				<img src={require('../img/farmer_01.jpg')} alt="farmerPic" />
				<h2>{user.firstName} {user.lastName}</h2>
				<h3>status:</h3>
			</div>
			<div>
				<form className="myFormACU" onSubmit={changeUser}>
					<div className="colContentACU">
						<div className="leftColACU">
							<label>Křestní jméno</label>
							<input type="text" id="fistName" name="firstName" value={firstName} onChange={changeFName}/>
							<label>Email</label>
							<input type="text" id="email" name="email" value={email} onChange={changeMail}/>
							<label>Datum narození</label>
							<input type="text" id="dateOfBirth" name="dateOfBirth" value={dateob} onChange={changeDOB}/>
						</div>
						<div className="rightColACU">
							<label>Příjmení</label>
							<input type="text" id="lastName" name="lastName" value={lastName} onChange={changeLName}/>
							<label>Telefonní číslo</label>
							<input type="text" id="phone" name="phone" value={phone} onChange={changePhone}/>
							<label>Č. bankovního účtu</label>
							<input type="text" id="bankAcc" name="bankAcc" value="mrdka"/>
						</div>
					</div>
					<div className="underColsACU">
						<input type="submit"/>
					</div>
					<div>
					</div>
				</form>		
			</div>
			
		</div>
	)
}

export default AdminChangeUser