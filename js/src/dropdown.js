export function attachDropdown(parent) {
  let dropdownDiv = document.createElement('div');
  dropdownDiv.classList.add('dropdown');

  let button = document.createElement('button');
  button.classList.add('dropbtn');
  button.innerHTML = 'Menu';
  dropdownDiv.appendChild(button);

  let dropdownContent = document.createElement('div');
  dropdownContent.classList.add('dropdown-content');
  dropdownDiv.appendChild(dropdownContent);

  let link1 = document.createElement('a');
  link1.href = '#';
  link1.innerHTML = 'Link 1';
  dropdownContent.appendChild(link1);

  let link2 = document.createElement('a');
  link2.href = '#';
  link2.innerHTML = 'Link 2';
  dropdownContent.appendChild(link2);

  let link3 = document.createElement('a');
  link3.href = '#';
  link3.innerHTML = 'Link 3';
  dropdownContent.appendChild(link3);

  parent.appendChild(dropdownDiv);

  window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName('dropdown-content');
      for (var i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  };
}
