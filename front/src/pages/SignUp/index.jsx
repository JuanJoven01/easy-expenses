import { useContext, useEffect } from "react"

import { GlobalContext } from "../../context"


export const SignUp = () => {

    const globalContext = useContext(GlobalContext)

    useEffect(() => {
        globalContext.setRoutesToShow(
            [
                {
                    'text': 'Back to Home',
                    'route': '/'
                }
            ]
        )
    },[])

    return (

        <h1>SignUp</h1>
    )
}