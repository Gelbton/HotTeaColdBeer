export const openModal = () => {
  const modal = document.querySelector(".details");

  modal.classList.add("show");
}

export const closeModal = () => {
  const modal = document.querySelector(".details");

  modal.classList.remove("show");
}