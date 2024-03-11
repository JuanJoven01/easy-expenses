import { createContext, useState } from "react";

export const GlobalContext = createContext()

export const GlobalProvider = (props) => {

    const [routesToShow, setRoutesToShow] = useState([])

    const [userLogged, setUserLogged] = useState(false)

    return(
        <GlobalContext.Provider value={{
            routesToShow,
            setRoutesToShow,
            userLogged,
            setUserLogged
        }}>
            {props.children}
        </GlobalContext.Provider>
    )
}