import { fetchData } from './fetchData';
import { renderData } from './renderData';

export const getForm = async event => {
  event.preventDefault();

  const detailsForm = document.querySelector(".details__form");
  const { from, to, vehicle } = event.target.elements;

  const data = await fetchData(from.value, to.value, vehicle.value);

  renderData(data);

  detailsForm.reset();
};
