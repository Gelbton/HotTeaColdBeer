export const renderData = data => {
  // const { duration, from, to, instructions } = data;
  // {text, street_name, street_destination, distance} = instructions;

  const detailsContainer = document.querySelector('.details__results'),
    detailsRoute = document.querySelector('.details__results-route'),
    detailsStart = document.querySelector('.details__results-start'),
    detailsEnd = document.querySelector('.details__results-end');

  detailsContainer.classList.remove('visually-hidden');

  detailsRoute.insertAdjacentHTML(
    'afterbegin',
    `
      <h2>Route:</h2>
      <p>${data.duration}</p>
    `
  );

  detailsStart.insertAdjacentHTML(
    'afterbegin',
    `
      <span class="details__results-circle"></span>
      <h3 class="details__results-title">${data.from}</h3>
    `
  );

  data.instructions.forEach(item => {
    console.log(item);

    const tr = document.createElement('tr');

    tr.insertAdjacentHTML(
      'afterbegin',
      `
        <td class="details__results-about">
          <svg width="23" height="32" viewBox="0 0 23 32" fill="currentColor"
            xmlns="http://www.w3.org/2000/svg">
            <path
              d="M11.4535 0.25L21.9414 12.2019C22.1499 12.4395 22.2126 12.7679 22.1058 13.063C21.9527 13.4861 21.5004 13.7221 21.0631 13.6247L20.9626 13.5963L14.1875 11.2557V31.75H8.8125V11.2234L1.94446 13.5963C1.6801 13.6876 1.38968 13.6521 1.15821 13.5053L1.06287 13.4357C0.716108 13.1454 0.652355 12.6524 0.897839 12.2897L0.965668 12.2019L11.4535 0.25Z"
              fill="currentColor" />
          </svg>

          <div class="details__results-descr">
            <h3>${item.text}</h3>
            <p>${item.street_name}</p>
          </div>
        </td>

        <td class="details__results-range">
          <p>${item.distance} km</p>
        </td>
      `
    );

    document.querySelector(".details__results-table tbody").appendChild(tr);
  });

  detailsEnd.insertAdjacentHTML(
    'afterbegin',
    `
      <span class="details__results-circle"></span>
      <h3 class="details__results-title">${data.to}</h3>
    `
  );
};
