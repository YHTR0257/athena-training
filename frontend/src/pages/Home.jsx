import { useNavigate } from 'react-router-dom'

function Home() {
  const navigate = useNavigate()

  return (
    <div>
      <h1>Athena Training</h1>
      <p>TODOアプリへようこそ</p>
      <button onClick={() => navigate('/todo')}>TODOリストへ</button>
    </div>
  )
}

export default Home
