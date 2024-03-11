import { useContext } from "react"
import { GlobalContext } from "../../context"
import { useNavigate } from "react-router-dom"


export const Navbar = () => {

    const navigate = useNavigate()

    const globalContext = useContext(GlobalContext)

    const printListItems = (objectWithRoutes) => {
        return (
            objectWithRoutes.map((item, index)=>(
                <li key={index} className="mx-2 hover:cursor-pointer hover:text-echo hover:underline" onClick={() => navigate(item.route)}>
                    {item.text}
                </li>
            ))
        )
        
    }

    return(
        <section className="h-14 text-slate-200 flex justify-between items-center border-b-[1px] border-slate-300 top-0 fixed w-full bg-opacity-50 backdrop-blur-lg ">
            <div>
                <h1 className="ml-2 hover:cursor-pointer hover:text-echo hover:underline" onClick={()=> navigate('/')}>EASY EXPENSES</h1>
            </div>
            <ul className="flex">
                {printListItems(globalContext.routesToShow)}
            </ul>
        </section>
    )
}