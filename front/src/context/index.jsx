import { createContext, useState } from "react";

export const GlobalContext = createContext()

export const GlobalProvider = (props) => {

    const [toTry, setToTry] = useState('Just to try')

    return(
        <GlobalContext.Provider value={{
            toTry,
            setToTry
        }}>
            {props.children}
        </GlobalContext.Provider>
    )
}