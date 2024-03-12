import { useContext, useEffect, useRef } from "react"

import { GlobalContext } from "../../context"

import { Title } from "../../components/Title"
import { TextBox } from "../../components/TextBox"
import { FormButton } from "../../components/FormButton"


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

    const username = useRef(null)
    const password = useRef(null)
    const password2 = useRef(null)

    return (
        <section className="min-h-[82vh] ">
        
        <Title text='SignUp'/>
        <TextBox text="Join and manage your expenses easily! Our app simplifies financial management, focusing on what's important. Sign up and improve your financial control." />
        
        <form className="mx-6 bg-slate-700 font-satoshi-italic p-4 rounded-lg flex flex-col text-slate-300">
            <label htmlFor="username" className="mb-4 flex">
                Username:
                <input ref={username} type="text" name="username" className="ml-4 grow bg-slate-500 px-2"/>
            </label>
            <label htmlFor="password" className="mb-4 flex">
                Password:
                <input ref={password} type="password" name="username" className="ml-4 grow bg-slate-500 px-2" />
            </label>
            <label htmlFor="username" className="flex">
                Repeat Password:
                <input ref={password2} type="password" name="username" className="ml-4 grow bg-slate-500 px-2" />
            </label>
            <div className='mt-4 flex justify-center'>
                <FormButton text='Sign Up'/>
            </div>

        </form>
        </section>
    )
}