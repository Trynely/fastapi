import axios from 'axios'
import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState([])

  useEffect(() => {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/items/',
      headers: {
        'Content-Type': 'application/json'
      }
    }).then((response) => {
      if(response.status === 200) {
        setCount(response.data)
      }
    })
  }, [])

  return (
    <>
      {
        count.map((el) => (
          <div>
            <p>{el.title}</p>
          </div>
        ))
      }
    </>
  )
}

export default App
