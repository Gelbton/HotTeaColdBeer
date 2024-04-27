export const getForm = (e) => {
  e.preventDefault();

  const target = e.target;

  console.log(target.vehicle.value);
  console.log(target.from.value);
  console.log(target.to.value);
}