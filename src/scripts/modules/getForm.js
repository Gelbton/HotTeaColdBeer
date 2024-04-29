import { fetchData } from './fetchData';
import { renderData } from './renderData';

export const getForm = async event => {
  event.preventDefault();

  const form = event.currentTarget;
  const { from, to, vehicle } = event.target.elements;

  const data = await fetchData(from.value, to.value, vehicle.value);

  console.log(data);

  const testData = {
    duration: '3 hrs 20 mins',
    from: 'Tokio, Japan',
    to: 'Incheon, South Korea',
    instructions: [
      {
        distance: 76,
        text: 'Continue onto Lindenschmitstraße',
        street_name: 'Lindenschmitstraße',
      },
      {
        distance: 6,
        text: 'Turn left onto Plinganserstraße and drive toward Zentrum',
        street_destination: 'Zentrum',
        street_name: 'Plinganserstraße',
      },
      {
        distance: 442,
        text: 'Turn right onto Radlkoferstraße',
        street_name: 'Radlkoferstraße',
      },
      {
        distance: 64,
        text: 'Turn right onto Hans-Fischer-Straße',
        street_name: 'Hans-Fischer-Straße',
      },
      {
        distance: 1512,

        text: 'Turn left onto Lindwurmstraße',
        street_name: 'Lindwurmstraße',
      },
    ],
  };

  renderData(testData);

  // form.reset();
};
