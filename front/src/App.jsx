import { BrowserRouter, useRoutes } from "react-router-dom"

import { GlobalProvider } from "./context"

import { Home } from "./pages/Home"
import { Navbar } from "./components/Navbar"
import { Footer } from "./components/Footer"
import { Login } from "./pages/Login"
import { Expenses } from "./pages/Expenses"
import { Reporters } from "./pages/Reporters"
import { Logout } from "./pages/Logout"
import { SignUp } from "./pages/SignUp"

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

  
  return (
    <div className="bg-slate-800 top-0 absolute w-full min-h-[100vh]">
      <BrowserRouter>
      <GlobalProvider>
          <Navbar />
          <div className='mt-16  '>
            <AppRoutes />
          </div>
          <Footer />
        </GlobalProvider>
      </BrowserRouter>
    </div>
  )
}

export default App
