import { useContext } from "react"
import { BrowserRouter, useRoutes } from "react-router-dom"
import { createPortal } from "react-dom"

import { GlobalContext } from "./context"

import { Home } from "./pages/Home"
import { Navbar } from "./components/Navbar"
import { Footer } from "./components/Footer"
import { Login } from "./pages/Login"
import { Expenses } from "./pages/Expenses"
import { Reporters } from "./pages/Reporters"
import { Logout } from "./pages/Logout"
import { SignUp } from "./pages/SignUp"
import { Error } from "./components/Error"
import { Loading } from "./components/Loading"

const AppRoutes = () => {

  const routes = useRoutes(
      [
        {path: '/', element: <Home/> },
        {path: '/login', element: <Login/> },
        {path: '/expenses', element: <Expenses/> },
        {path: '/reporters', element: <Reporters/> },
        {path: '/logout', element: <Logout/> },
        {path: '/signup', element: <SignUp/> },
      ]
  )
  return routes
}

function App() {

  const globalContext = useContext(GlobalContext)

  return (
    <div className="bg-slate-800 top-0 absolute w-full min-h-[100vh]">
      <BrowserRouter>
          <Navbar />
          <div className='mt-16  '>
            {globalContext.inError[0] && createPortal(<Error text={globalContext.inError[1]} />, document.body)}
            {globalContext.loading && createPortal(<Loading />, document.body)}
            <AppRoutes />
          </div>
          <Footer />
      </BrowserRouter>
    </div>
  )
}

export default App
