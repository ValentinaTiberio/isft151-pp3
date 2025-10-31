export class AdopcionForm extends HTMLElement {
  constructor() {
    super();
    this.innerHTML = `
      <form id="adopcionForm">
        <input type="number" id="user_id" placeholder="ID Usuario" required><br>
        <input type="number" id="animal_id" placeholder="ID Animal" required><br>
        <button type="submit">Enviar solicitud</button>
      </form>
    `;
  }

  connectedCallback() {
    this.querySelector("#adopcionForm").addEventListener("submit", async (e) => {
      e.preventDefault();
      const user_id = this.querySelector("#user_id").value;
      const animal_id = this.querySelector("#animal_id").value;

      const res = await fetch("http://127.0.0.1:5000/api/adopciones/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ user_id, animal_id })
      });

      const data = await res.json();
      alert("Solicitud creada con estado: " + data.estado);
    });
  }
}

customElements.define("adopcion-form", AdopcionForm);
