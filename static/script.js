  window.addEventListener('load', () => {
    setTimeout(() => {
      document.getElementById('popupMenu').style.display = 'block';
     
    }, 500); 

    document.getElementById('overlay').addEventListener('click', () => {
      document.getElementById('popupMenu').style.display = 'none';
      document.getElementById('overlay').style.display = 'none';
    });
  });




document.querySelector("#close").addEventListener
("click",function()
{
document.querySelector(".popup").style.display="none";
}
);