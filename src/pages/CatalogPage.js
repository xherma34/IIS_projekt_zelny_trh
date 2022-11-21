import React, {useState, useEffect, useContext} from 'react'
import AuthContext from '../context/AuthContext'
import useAxios from '../utils/useAxios'
import './catalogPage.css'


const CatalogPage = () => {

	let [catalog, setCatalogType] = useState([])

	useEffect(()=> {
		getCatalog()
	  }, [])


	let api = useAxios()

	let getCatalog = async() =>{
		let response = await api.get('/api/cropCatalogList/')

		if(response.status === 200){
			setCatalogType(response.data)
		}
		
	}

  return (
	
	<div>
		<div className="header">
			<div className="header-left">
				<img src={require('../img/home.png')}/>
			</div>

			<div className="header-search-container">
				<div className="header-search">
					<p>TEST</p>
				</div>
			</div>

			<div className="header-right">
				<img src={require('../img/home.png')} />
			</div>
		</div>



		<div className="filter-parent">
			<h2>Filtrovat podle</h2>
			<div className="filter-container">
				<div className="filter-items">
					<div className="filter-item">
						<p>Zelenina</p>	
					</div>

					<div className="filter-item">
						<p>Ovoce</p>
					</div>
				</div>
			</div>
		</div>


		

					{catalog.map(catalog=> (
						<div className="catalog-container">
							<div className="catalog-item">
								<img src={require('../img/apple.jpg')} alt="catalog_type" />
								<h2 key={catalog.cropType}>{catalog.cropType}</h2>
								<p key={catalog.image}>{catalog.category}</p>
							</div>
						</div>
					))}
			
	</div>
  )
}

export default CatalogPage;