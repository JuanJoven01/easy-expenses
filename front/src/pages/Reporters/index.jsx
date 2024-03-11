import { useEffect, useContext } from "react"

import { GlobalContext } from "../../context"

export const Reporters = () => {

    const globalContext = useContext(GlobalContext)

    useEffect(() => {
        globalContext.setRoutesToShow(
            [
                {
                    'text': 'Logout',
                    'route': '/logout'
                }
            ]
        )
    },[])

    return(
        <>
            <h1>Reporters</h1>
        </>

    )
}