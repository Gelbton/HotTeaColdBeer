import { API_URI } from '../const.js';

export const fetchData = async (from, to, vehicle) => {
  const detailsLoader = document.querySelector('.details__loader'),
    detailsSubmitBtn = document.querySelector('.details__submit'),
    detailsError = document.querySelector(".details__error"),
    line = document.querySelector(".details__line"),
    detailsContainer = document.querySelector('.details__results');


  detailsLoader.classList.remove('visually-hidden');
  detailsSubmitBtn.classList.add('visually-hidden');
  line.classList.remove('visually-hidden');
  detailsError.classList.add("visually-hidden");
  detailsContainer.classList.add("visually-hidden");


  const query = new URLSearchParams({
    transportation_type: vehicle,
    from_city: from,
    to_city: to,
  });

  try {
    const response = await fetch(`${API_URI}path?${query.toString()}`, {
      method: 'GET',
    });

    if (!response.ok) {
      throw new Error('Failed to fetch data');
    }

    detailsError.classList.add("visually-hidden");

    return await response.json();
  } catch (error) {
    detailsError.classList.remove("visually-hidden");
    throw new Error(error.message);
  } finally {
    detailsLoader.classList.add('visually-hidden');
    detailsSubmitBtn.classList.remove('visually-hidden');
  }
};
