import React, {useState, useEffect, useContext} from 'react'
import AuthContext from '../context/AuthContext'
import useAxios from '../utils/useAxios'
import './cropPage.css'

const CropPage = () => {


	let [crop, setCrop] = useState([])

	useEffect(()=> {
		getCrop()
	  }, [])


	let api = useAxios()

	let getCrop = async() =>{
		let response = await api.get('/api/getAllCrop/')

		if(response.status === 200){
			setCrop(response.data)
		}
	}



	// let GetFarmer = async() =>{
		
	// 	let response = await api.get('/api/userDetail/'+1)

	// 	console.log('farmari:', response.data)

	// 	if(response.status === 200){
	// 		setFarmer(response.data)
			
	// 	}
		
	// }

  return (
	<div>
		<div className="header">
			<div className="header-left">
				<img src={require('../img/home.png')} />
			</div>

			<div className="header-search-container">
				<div className="header-search">
					<p>TEST</p>
				</div>
			</div>

			<div className="header-right">
				<img src={require('../img/burger-menu.png')} />
			</div>
		</div>



		<div className="filter-parent">
			<h2>Plodiny k prodeji</h2>
			<div className="filter-container">
				<div className="filter-items">
					<div className="filter-item">
						<p>Max. Cena/kg</p>	
					</div>

					<div className="filter-item">
						<p>Max. Cena/kus</p>
					</div>

					<div className="filter-item">
						<p>Farmář</p>
					</div>

					<div className="filter-item">
						<p>Místo původu</p>
					</div>

					<div className="filter-item">
						<p>Množství</p>
					</div>
				</div>
			</div>
		</div>

		{crop.map(crop=> (
			<div className="crop-container">
			<div className="crop-item">
				<img src={require('../img/apple.jpg')} alt="crop_img" />
				<h2>{crop.name}</h2>
				<div className="farmer-img">
					<img src={require('../img/farmer_01.jpg')} alt="farmer_img" />	
				</div>

				{/* {farmer.map(farmer=> (
				<p key={farmer.id}>{farmer.full_name}</p>
				))}	 */}

				<p>{crop.farmer.full_name}</p>

				<div className="crop-row">
					<p>Místo původu: {crop.placeOfOrigin}</p>
				</div>

				<div className="crop-row">
					<p>Skladem: {crop.amount}</p>
				</div>

				<div className="crop-row">
					<p>Cena/kg: {crop.price}</p>
				</div>

				<div className="crop-row">
					<p>Vaše množství:</p>
				</div>

				<div className="button-container">
					<a href="">Koupit</a>
				</div>
			</div>

		</div>
		))}

		

	</div>
  );
}

export default CropPage;
