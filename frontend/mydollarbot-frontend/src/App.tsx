import './App.css'
import { useEffect, useState } from 'react';
import { getData } from './api/index'

import { Table, Card, Divider, Typography } from 'antd'; // Importing antd components

function App() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    async function fetchData() {
      const response = await getData();
      const data = await response.json();
      setData(data);
    }
    fetchData();
  }, []);

  // Columns for the budget table
  const budgetColumns = [
    {
      title: 'Category',
      dataIndex: 'category',
    },
    {
      title: 'Allocated',
      dataIndex: 'allocated',
    },
    {
      title: 'Spent',
      dataIndex: 'spent',
    },
    {
      title: 'Remaining',
      dataIndex: 'remaining',
    }
  ];

  // Columns for the spendings table
  const spendingsColumns = [
    {
      title: 'Category',
      dataIndex: 'category',
    },
    {
      title: 'Amount',
      dataIndex: 'amount',
    },
    {
      title: 'Description',
      dataIndex: 'description',
    },
    {
      title: 'Date',
      dataIndex: 'date',
    }
  ];

  return (
    <>
      {data ? (
        <>
          <Typography.Title level={2}>Budget Data</Typography.Title>
          <Table dataSource={data.budget_data} columns={budgetColumns} pagination={false} />
          
          <Divider />

          <Typography.Title level={2}>Spendings</Typography.Title>
          <Table dataSource={data.spendings} columns={spendingsColumns} pagination={false} />
          
          <Divider />

          <Typography.Title level={2}>Categories</Typography.Title>
          <Card>
            {data.categories.map((cat: any) => (
              <Card.Grid key={cat.id} style={{ width: '20%', textAlign: 'center' }}>
                {cat.name}
              </Card.Grid>
            ))}
          </Card>
        </>
      ) : (
        <p>loading...</p>
      )}
    </>
  )
}

export default App;
