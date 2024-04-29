import { API_KEY } from '../const';

export const fetchData = async (from, to, vehicle) => {
  const query = new URLSearchParams({ from, to, vehicle });

  console.log("query: ", query.toString());

  try {
    const response = await fetch(
      `https://graphhopper.com/api/1/geocode?q=${from}&locale=en&limit=2&key=${API_KEY}`,
      { method: 'GET' }
    );

    return await response.json();
  } catch (error) {
    throw new Error(error.message);
  }
};
