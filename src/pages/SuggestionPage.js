import React, {useState, useEffect, useContext} from 'react'
import AuthContext from '../context/AuthContext'
import useAxios from '../utils/useAxios'
import './suggestionPage.css'




const SuggestionPage = () => {

	let [suggestion, setSuggestion] = useState([])
	let [suggestionDel, setSuggestionDel] = useState([])
	useEffect(()=> {
		getSuggestion()
	  }, [])


	let api = useAxios()

	let getSuggestion = async() =>{
		let response = await api.get('/api/getAllSuggestions/')
		
		if(response.status === 200){
			setSuggestion(response.data)
		}

	}
	

	// let suggestionDelete = async() => {
	// 	let response = await api.get('/api/suggestionDelete/5')
		
	// 	};

	async function suggestionDelete(suggestion) {
		// let x = JSON.parse(this.state.suggestion)
		// console.log('tady je ten param:', suggestion.suggestion['id'])
		let suggestionID = suggestion.suggestion['id']
		let response = await api.get('/api/suggestionDelete/'+suggestionID)
		alert(`hello, ${'/api/suggestionDelete/'+suggestionID}`);
	  }

	async function suggestionCreate(suggestion) {
	// let x = JSON.parse(this.state.suggestion)
	 console.log('tady je Create:', JSON.stringify(suggestion.suggestion))
		let response = await api.get('/api/cropCatalogCreate/'+JSON.stringify(suggestion.suggestion))
	//  let response = await api.get('/api/cropCatalogCreate/'+"{cropType"+":"+"Hovno"+","+"category"+":"+"Ovoce}")
	// let suggestionID = suggestion.suggestion['id']
	// let response = await api.get('/api/suggestionCreate/'+suggestionID)
	// alert(`hello, ${'/api/suggestionDelete/'+suggestionID}`);
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
		<img src={require('../img/burger-menu.png')}/>
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

{suggestion.map(suggestion=> (
			<div className="crop-container">
			<div className="crop-item">
				<img src={require('../img/apple.jpg')} alt="crop_img"/>
				<h2>{suggestion.name}</h2>
				<div className="farmer-img">
					<img src={require('../img/farmer_01.jpg')} alt="farmer_img"/>	
				</div>
		
				<div className="crop-row">
					<p>Druh: {suggestion.croptype}</p>
				</div>
		
				<div className="crop-row">
					<p>Kategorie: {suggestion.category}</p>
				</div>
		
				<div className="button-container">
					<a onClick={() => suggestionDelete({suggestion})}>Zamítnout</a>
					<a onClick={() => suggestionCreate({suggestion})}>Schválit</a>
				</div>
			</div>
		
		</div>
		))}


	</div>
  )
}

export default SuggestionPage
