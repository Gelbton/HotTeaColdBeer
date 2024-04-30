import { getDirectionIcon } from './getDirectionIcon';

export const renderData = data => {
  const { hr, min, origin: from, destination: to, instructions } = data;

  const detailsContainer = document.querySelector('.details__results'),
    detailsRoute = document.querySelector('.details__results-route'),
    detailsStart = document.querySelector('.details__results-start'),
    detailsEnd = document.querySelector('.details__results-end'),
    detailsTableBody = document.querySelector('.details__results-table tbody');

  detailsRoute.innerHTML = '';
  detailsStart.innerHTML = '';
  detailsEnd.innerHTML = '';
  detailsTableBody.innerHTML = '';

  detailsContainer.classList.remove('visually-hidden');

  

  const time = hr > 0 ? `${hr} hrs ${min} mins` : `${min} mins`;

  detailsRoute.insertAdjacentHTML(
    'afterbegin',
    `
      <h2>Route:</h2>
      <p>${time}</p>
    `
  );

  detailsStart.insertAdjacentHTML(
    'afterbegin',
    `
      <span class="details__results-circle"></span>
      <h3 class="details__results-title">${from}</h3>
    `
  );

  instructions.forEach(item => {
    const tr = document.createElement('tr');

    tr.insertAdjacentHTML(
      'afterbegin',
      `
        <td class="details__results-about">
          ${getDirectionIcon(item.path).outerHTML}

          <div class="details__results-descr">
            <h3>${item.path}</h3>
            <p>${item.street}</p>
          </div>
        </td>

        <td class="details__results-range">
          <p>${item.distance_km} km</p>
        </td>
      `
    );

    detailsTableBody.appendChild(tr);
  });

  detailsEnd.insertAdjacentHTML(
    'afterbegin',
    `
      <span class="details__results-circle"></span>
      <h3 class="details__results-title">${to}</h3>
    `
  );
};
