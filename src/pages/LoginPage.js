import React, {useState, useEffect, useContext} from 'react'
import AuthContext from '../context/AuthContext'
import useAxios from '../utils/useAxios'
import './loginPage.css'

const LoginPage = () => {
	let {loginUser} = useContext(AuthContext)
  	return (
	<div>
		<div className="header">
			<div className="header-left">
				<img src="img/home.png" />
			</div>

			<div className="header-right">
				<img src="img/burger-menu.png" />
			</div>
		</div>

		<div className="main">
			<div className="container">
				<div className="left">
					<form onSubmit={loginUser}>
						<div className="container-left">
							<h1>Vítame Vás!</h1>
							<div className="container-form">
								<label>Email:</label>
								<input type="text" id="mail" name="email" placeholder="Your email:"/>
								<label>Password:</label>
								<input type="password" name="password" placeholder="Your password:"/>
								<p>Zapomněli jste heslo?</p>
								<input type="submit" name="submit" value="Přihlásit se"/>
								<p>Ještě nemáte účet? <a href="./registerPage">Zaregistrujte se zde!</a></p>
							</div>
						</div>
					</form>
				</div>

				<div className="right">
					<div className="container-right">
						<h1>Zelný Trh</h1>
						<hr/>
						<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
						tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
						quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
						consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
						cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
						proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
						<h2>Pokračovat bez registrace</h2>

						<div className="continue-img">
							<img src="img/continue.png" alt="continue.jpg" />
						</div>
					</div>
				</div>
			</div>
		</div>

		<div className="footer">
	
		</div>
	</div>
  )
}

export default LoginPage;

