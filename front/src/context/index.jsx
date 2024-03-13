import { createContext, useState } from "react";

export const GlobalContext = createContext()

export const backHost = 'https://easy-expenses-back.onrender.com'

export const GlobalProvider = (props) => {

    const [routesToShow, setRoutesToShow] = useState([])
    const [userLogged, setUserLogged] = useState(false)
    const [inError, setInError] = useState([false, null])
    const [loading, setLoading] = useState(false)

    return(
        <GlobalContext.Provider value={{
            routesToShow,
            setRoutesToShow,
            userLogged,
            setUserLogged,
            inError,
            setInError,
            loading,
            setLoading
        }}>
            {props.children}
        </GlobalContext.Provider>
    )
}