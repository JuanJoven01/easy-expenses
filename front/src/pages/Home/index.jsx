import { useContext, useEffect } from "react"
import { GlobalContext } from "../../context"

import { Title } from "../../components/Title"
import { TextBox } from "../../components/TextBox"
import { BasicButton } from "../../components/BasicButton"
import { useNavigate } from "react-router"

export const Home = () => {
    const navigate = useNavigate()

    const globalContext = useContext(GlobalContext)

    useEffect(() => {
        globalContext.setRoutesToShow(
            [
                {
                    'text': 'Login',
                    'route': '/login'
                }
            ]
        )
    },[])

    return (
        <section className="min-h-[82vh] ">
            <Title text='Home' />
            <TextBox text="In our simple expense tracker, we focus on what truly matters: managing your expenses without unnecessary complexity. Start taking control of your finances effortlessly today." />
            <div className="flex justify-center" >
                <div className="px-2" onClick={() => navigate('/login')}>
                    <BasicButton text='LogIn'/>
                </div>
                <div className="px-2" onClick={() =>  navigate('/signup')}>
                    <BasicButton text='SignUp'/>
                </div>
            </div>
            
        
        </section>
    )
}