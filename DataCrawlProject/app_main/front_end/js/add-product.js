const form = document.querySelector('#insert-data-form');
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const glasses_id = document.querySelector('#glasses_id').value;
  const link = document.querySelector('#link').value;
  const glasses_name = document.querySelector('#glasses_name').value;
  const brand_name = document.querySelector('#brand_name').value;
  const price = document.querySelector('#price').value;
  const img_url = document.querySelector('#img_url').value;
  
  fetch(`http://127.0.0.1:9001/insert?glasses_id=${glasses_id}&link=${link}&glasses_name=${glasses_name}&brand_name=${brand_name}&price=${price}&img_url=${img_url}`, {
    method: 'POST'
  })
  .then(response => response.json())
  .then(data => {
    alert("Inserted successfully");
    console.log(data);
  })
  .catch(error => console.log(error));
});