export class AnimalList extends HTMLElement {
  constructor() {
    super();
    this.innerHTML = `
      <h2>Lista de animales</h2>
      <table border="1" cellpadding="5">
        <thead>
          <tr><th>ID</th><th>Nombre</th><th>Especie</th><th>Estado</th><th>Fecha de ingreso</th></tr>
        </thead>
        <tbody id="tablaAnimales"></tbody>
      </table>
    `;
  }

  connectedCallback() {
    this.loadAnimals();
  }

  async loadAnimals() {
    const res = await fetch("http://127.0.0.1:5000/api/animals/");
    const data = await res.json();

    const tbody = this.querySelector("#tablaAnimales");
    tbody.innerHTML = data.map(a => `
      <tr>
        <td>${a.id}</td>
        <td>${a.nombre}</td>
        <td>${a.especie}</td>
        <td>${a.estado}</td>
        <td>${a.fecha_ingreso}</td>
      </tr>
    `).join("");
  }
}

customElements.define("animal-list", AnimalList);
