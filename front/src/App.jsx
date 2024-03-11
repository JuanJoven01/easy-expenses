import { createBrowserRouter, RouterProvider } from "react-router-dom"

import { GlobalProvider } from "./context"

import { Home } from "./pages/Home"
import { Navbar } from "./components/Navbar"
import { Footer } from "./components/Footer"

function App() {

  const router = createBrowserRouter([
    {path: '/', element: <Home/> },

  ])

  return (
    <>
      <GlobalProvider>
        <Navbar />
        <RouterProvider router={router} />
        <Footer />
      </GlobalProvider>
      
    </>
  )
}

export default App
