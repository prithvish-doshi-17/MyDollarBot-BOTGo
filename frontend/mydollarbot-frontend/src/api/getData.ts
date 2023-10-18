export async function getData(): Promise<Response> {
  const data = await fetch('/api/dummyData')
  return data;
}

