// ********** set date ************
// select span
const date = (document.getElementById('date').innerHTML =
  new Date().getFullYear())

// ********** nav toggle ************
// select button and links
const navBtn = document.getElementById('nav-toggle')
const links = document.getElementById('nav-links')
// add event listener
navBtn.addEventListener('click', () => {
  links.classList.toggle('show-links')
})

// ********** smooth scroll ************
// select links
// add click event listener to all links
const navLinks = document.querySelectorAll('.nav-links a');
navLinks.forEach((link) => {
  link.addEventListener('click', (e) => {
    // prevent default link behavior
    e.preventDefault();

    // remove the 'show-links' class from the links
    links.classList.remove('show-links');

    // scroll to the element with the corresponding ID
    const targetId = link.getAttribute('href');
    const targetElement = document.querySelector(targetId);
    targetElement.scrollIntoView({ behavior: 'smooth' });
  });
});
//In this code, we add a click event listener to all the links in the navigation menu using querySelectorAll.
// Then, in the event listener function, we first prevent the default link behavior using preventDefault().
// Next, we remove the show-links class from the links element to hide the navigation menu.
// Finally, we use the scrollIntoView() method to scroll to the element with the corresponding ID,
// and we specify the smooth behavior to make the scrolling animation smoother.