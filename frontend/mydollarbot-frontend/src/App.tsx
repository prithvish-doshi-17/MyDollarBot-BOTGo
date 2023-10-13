import './App.css'
import { useEffect, useState } from 'react';
import { getData } from './api/index'

function App() {
  const [data, setData] = useState<string | null>(null);

  useEffect(() => {
    async function fetchData() {
      const response = await getData();
      const data = await response.text();
      setData(data);
    }
    fetchData();
  }, []);

  return (
    <>
      {data && <>{data}</>}
      <p>more data</p>
      <p>This is a test</p>
    </>
  )
}

export default App;
