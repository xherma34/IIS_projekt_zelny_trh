import React, {useState, useEffect, useContext} from 'react'
import AuthContext from '../context/AuthContext'
import useAxios from '../utils/useAxios'
import './AdminPage.css'
import {Link} from 'react-router-dom'

const AdminPage = () => {

	let[users, setUsers] = useState([])

	let ran = 0

	useEffect(() => {
		
		getUsers()
		
	}, [])

	let api = useAxios()

	let getUsers = async() =>{
		let response = await api.get('/api/userList/')

		if(response.status === 200)
		{
			setUsers(response.data)
		}
	}

	async function deleteUser(user)
	{
		let response = await api.get('/api/userDelete/'+user.id)

	}

	return(
		<div className='contentAP'>
			{users.map(users =>(
				<div className='rowAP'>
					<div className='firstColAP'>
						<div className='picAP'>
							<img src={require('../img/farmer_01.jpg')} alt="farmerPic" />
						</div>
						<div>
							<div className="myTextRow">
								<p className='nameAP'>{users.firstName}</p>
								<p className='nameAP'>{users.lastName}</p>
							</div>
							<p className='mailAP'>{users.email}</p>
						</div>
						<div>
							{users.image}
						</div>
					</div>
					<div className='secondColAP'>
						<div className='buttonAP'>
							<img src={require('../img/farmer_01.jpg')} alt="farmerPic" />
							<Link to={'/changeuser/'+users.id}>
								<button>Upravit</button>
							</Link>
						</div>
						<div className='buttonAP'>
							<img src={require('../img/farmer_01.jpg')} alt="farmerPic" />
							<button
							type="submit"
							onClick={() => {deleteUser(users)}}
							>Smazat</button>
						</div>
					</div>
				</div>

			))}
		</div>
		
	)
};

export default AdminPage;

