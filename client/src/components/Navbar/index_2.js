import React from "react";
import { Nav, NavLink, NavMenu }
	from "./NavbarElements"

const Navbar2 = () => {
return (
	<>
	<Nav>
		<NavMenu>
			<NavLink to="/list_Documents" activeStyle>
				List_documents
			</NavLink>
		</NavMenu>
	</Nav>
	</>
);
};

export default Navbar2;
