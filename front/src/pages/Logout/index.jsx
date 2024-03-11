import { useContext, useEffect } from "react"
import { GlobalContext } from "../../context"


export const Logout = () => {

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
                Logout
            </section>
        </>
    )
}