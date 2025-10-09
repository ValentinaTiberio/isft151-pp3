export class AnimalForm extends HTMLElement {
  constructor() {
    super();
    this.innerHTML = `
      <form id="animalForm">
        <input type="text" id="nombre" placeholder="Nombre del animal" required><br>
        <input type="text" id="especie" placeholder="Especie" required><br>
        <input type="text" id="estado" placeholder="Estado (ej. Rescatado, En tratamiento)" required><br>
        <button type="submit">Registrar</button>
      </form>
      <hr>
    `;
  }

  connectedCallback() {
    const form = this.querySelector("#animalForm");
    form.addEventListener("submit", async (e) => {
      e.preventDefault();

      const nombre = this.querySelector("#nombre").value;
      const especie = this.querySelector("#especie").value;
      const estado = this.querySelector("#estado").value;

      const res = await fetch("http://127.0.0.1:5000/api/animals/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nombre, especie, estado })
      });

      const data = await res.json();
      alert("Animal registrado correctamente 🐾");

      // Notificar al componente de lista para que se actualice
      document.querySelector("animal-list").loadAnimals();
      form.reset();
    });
  }
}

customElements.define("animal-form", AnimalForm);
