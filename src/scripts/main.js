import 'normalize.css'
import '../scss/index.scss'
import { closeModal, openModal } from './modules/modal';
import { getForm } from './modules/getForm';


const openBtn = document.querySelector(".menu-btn"),
  closeBtn = document.querySelector(".details__close"),
  detailsForm = document.querySelector(".details__form");

openBtn.addEventListener("click", openModal);
closeBtn.addEventListener("click", closeModal);
detailsForm.addEventListener("submit", (event) => getForm(event));