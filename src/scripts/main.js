import 'normalize.css'
import '../scss/index.scss'
import { closeModal, openModal } from './modules/modal';

// import {getForm} from "./modules/getForm.js"

// const form = document.querySelector("#gps");
// const btn = document.querySelector("button");

// form.addEventListener("submit", (e) => getForm(e));


const openBtn = document.querySelector(".menu-btn"),
  closeBtn = document.querySelector(".details__close");

openBtn.addEventListener("click", openModal);
closeBtn.addEventListener("click", closeModal);