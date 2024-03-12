import { useContext, useEffect, useRef } from "react"

import { GlobalContext } from "../../context"

import { Title } from "../../components/Title"
import { TextBox } from "../../components/TextBox"
import { FormButton } from "../../components/FormButton"
import { useNavigate } from "react-router"


export const Login = () => {

    const navigate = useNavigate()

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

    const username = useRef(null)
    const password = useRef(null)

    

    return (
        <section className="min-h-[82vh] ">
        
        <Title text='Login'/>
        <TextBox text="Welcome back! Log in to our expense management app and quickly access your financial records. With a simple and secure login process, you can keep track of your expenses. Control your finances easily and effectively!" />
        
        <form className="mx-6 bg-slate-700 font-satoshi-italic p-4 rounded-lg flex flex-col text-slate-300">
            <label htmlFor="username" className="mb-4 flex">
                Username:
                <input ref={username} type="text" name="username" className="ml-4 grow bg-slate-500 px-2"/>
            </label>
            <label htmlFor="password" className="mb-4 flex">
                Password:
                <input ref={password} type="password" name="username" className="ml-4 grow bg-slate-500 px-2" />
            </label>
            
            <div className='mt- flex justify-center'>
                <FormButton text='Login'/>
            </div>

            <div className="mt-2" onClick={()=> {navigate('/signup')}}>
                <p className="text-center">Have not got an user?</p>
                <p className="text-center text-delta hover:underline">Go to SignUp</p>
            </div>

        </form>
        
        </section>
    )
}