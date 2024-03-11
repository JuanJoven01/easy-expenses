import { useContext } from "react"
import { GlobalContext } from "../../context"



export const Home = () => {

    const globalContext = useContext(GlobalContext)

    return (
        <>
            <h1>Home</h1>
            <h1>{globalContext.toTry}</h1>
        </>
    )
}