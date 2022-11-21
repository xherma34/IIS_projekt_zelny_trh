import "./UserInfoPage.css"
import React, {useState, useEffect, useContext} from 'react'
import AuthContext, { AuthProvider } from '../context/AuthContext'
import useAxios from '../utils/useAxios'

const UserInfoPage = () => {

	let {user, logoutUser} = useContext(AuthContext)

	return (
		<div className='contentUIP'>
			<h1>Vítejte na Vašem profilu!</h1>
			<div className='leftColUIP'>
				<div className='picUIP'>
					<img src={require('../img/farmer_01.jpg')} alt="farmerPic" />
				</div>
				<div className='nameUIP'>
					<h3>Jméno: {user.full_name}</h3>
				</div>
				<div className='buttonsColUIP'>
					<button>Moje objednávky</button>
					<button>Moje události</button>
					<button>Moje nabídky</button>
					<button>Odhlásit se</button>
				</div>
			</div>
			<div className='rightColUIP'>
				<div className='left'>
					<label>E-mail:</label>
					<input type="text" id="mail" name="email" placeholder="email"/>
					<label>Datum narození:</label>
					<input type="text" id="BirthDate" name="BirthDate" placeholder="BirthDate"/>
				</div>
				<div className='right'>
					<label>Telefonní číslo</label>
					<input type="text" id="phoneNumber" name="phoneNumber" placeholder="phoneNumber"/>
					<label>Č. bankovního účtu</label>
					<input type="text" id="bankAcc" name="bankAcc" placeholder="bankAcc"/>
				</div>
				<div className='under'>
					<button>Potvrdit</button>
				</div>
			</div>
		</div>
  );
}

export default UserInfoPage