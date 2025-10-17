export class AnimalForm extends HTMLElement {
  constructor() {
    super();
    this.innerHTML = `
      <form id="animalForm" enctype="multipart/form-data">
        <input type="text" id="nombre" placeholder="Nombre del animal" required><br>
        <input type="text" id="especie" placeholder="Especie" required><br>
        <input type="text" id="estado" placeholder="Estado (ej. Rescatado, En tratamiento)" required><br>
        <input type="file" id="foto" accept="image/*"><br>
        <button type="submit">Registrar</button>
      </form>
      <hr>
    `;
  }

  connectedCallback() {
    const form = this.querySelector("#animalForm");
    form.addEventListener("submit", async (e) => {
      e.preventDefault();

      const formData = new FormData();
      formData.append("nombre", this.querySelector("#nombre").value);
      formData.append("especie", this.querySelector("#especie").value);
      formData.append("estado", this.querySelector("#estado").value);
      const foto = this.querySelector("#foto").files[0];
      if (foto) formData.append("foto", foto);

      const res = await fetch("http://127.0.0.1:5000/api/animals/", {
        method: "POST",
        body: formData
      });

      const data = await res.json();
      alert("Animal registrado correctamente");
      document.querySelector("animal-list").loadAnimals();
      form.reset();
    });
  }
}

customElements.define("animal-form", AnimalForm);
