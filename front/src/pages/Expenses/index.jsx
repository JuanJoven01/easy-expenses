import { useEffect, useContext } from "react"

import { GlobalContext } from "../../context"

export const Expenses = () => {

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
        <h1>Expenses</h1>
        </>

    )
}