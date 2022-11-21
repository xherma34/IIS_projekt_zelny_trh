import React, {useState, useEffect, useContext} from 'react'
import AuthContext from '../context/AuthContext'
import useAxios from '../utils/useAxios'
import './registerPage.css'

const RegisterPage = () => {
	let {loginUser} = useContext(AuthContext)
	return (
	<div>
		<div class="header">
			<div class="header-left">
				<img src="img/home.png"/>
			</div>

			<div class="header-right">
				<img src="img/burger-menu.png"/>
			</div>
		</div>

		<div class="main">
			<div class="container">
				<div class="left">
					<form action="" method="POST">
						<div class="container-left">
							<h1>Vytvořte si účet!</h1>
							<div class="container-form">
								<div class="container-form-items">
									<div class="container-form-item1">
										<label>Jméno:</label>
										<input type="text" id="mail" name="email" placeholder="Your email:"/>
									</div>
									<div class="container-form-item2">
										<label>Příjmení:</label>
										<input type="password" name="password" placeholder="Your password:"/>
									</div>
								</div>
								<label>Email:</label>
								<input type="text" id="mail" name="email" placeholder="Your email:"/>
								<label>Heslo:</label>
								<input type="password" name="password" placeholder="Your password:"/>
								<label>Potvrzení hesla:</label>
								<input type="password" name="password2" placeholder="Repeat password:"/>
								<input type="submit" name="submit" value="Registrovat se"/>
							</div>
						</div>
					</form>
				</div>
				<div class="right">
					<div class="container-right">
						<h1>Již máte účet?</h1>
						<form onSubmit={loginUser}>
						<div class="container-left">
							<div class="container-form-right">
								<label>Email:</label>
								<input type="text" id="mail" name="email" placeholder="Your email:"/>
								<label>Heslo:</label>
								<input type="password" name="password" placeholder="Your password:"/>
								<p>Zapomněli jste heslo?</p>
								<input type="submit" name="submit" value="Přihlásit se"/>
							</div>
						</div>
					</form>

					</div>
				</div>
			</div>
		</div>


		<div class="footer">
			
		</div>

	</div>
  )
}

export default RegisterPage;