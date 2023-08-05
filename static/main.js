// Realtime Database
const pin = document.getElementById("pincode");
const date = document.getElementById("date");
const btnSubmit = document.getElementById("submit");

const database = firebase.database();
const rootRef = database.ref('/users/');

btnSubmit.addEventListener('click', (e)=> {
  const autoId = rootRef.push().key
  rootRef.child(autoId).set({
    pin: pin.value,
    date: date.value
  });
});

// Onclick functions
function github(){
  window.open('https://github.com/AkhileshThite')
}

function feedback(){
  window.open('/feedback','_self')
}

function source() {
  alert('Are you a developer? would you like to contribute to this project?');
  window.open('https://github.com/AkhileshThite/COVID-19-VaccineFinder');
}
