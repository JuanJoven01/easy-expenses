import { useContext, useEffect } from "react"
import { GlobalContext } from "../../context"


export const Login = () => {

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
    
    
    return(
        <>
            <section>
                Login
            </section>
        </>
    )
}