const template = document.createElement("template");
template.innerHTML = `
  <style>
    .solicitud-card {
      background: white;
      padding: 15px;
      border-radius: 10px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      margin-bottom: 10px;
    }
    .solicitud-card p {
      margin: 5px 0;
    }
    .btn-estado {
      background-color: orange;
      color: white;
      border: none;
      padding: 5px 10px;
      border-radius: 5px;
      cursor: pointer;
    }
    .btn-estado:hover {
      background-color: #e69500;
    }
  </style>
  <div id="solicitudesContainer"></div>
`;

class AdopcionList extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });
    this.shadowRoot.appendChild(template.content.cloneNode(true));
  }

  async connectedCallback() {
    await this.loadSolicitudes();
  }

  async loadSolicitudes() {
    const res = await fetch("http://127.0.0.1:5000/api/adopciones/");
    const solicitudes = await res.json();
    const container = this.shadowRoot.getElementById("solicitudesContainer");
    container.innerHTML = solicitudes.map(s => `
      <div class="solicitud-card">
        <p><strong>ID Solicitud:</strong> ${s.id}</p>
        <p><strong>Animal ID:</strong> ${s.animal_id}</p>
        <p><strong>Usuario ID:</strong> ${s.user_id}</p>
        <p><strong>Estado:</strong> ${s.estado}</p>
        <button class="btn-estado" data-id="${s.id}" data-estado="Aprobada">Aprobar</button>
        <button class="btn-estado" data-id="${s.id}" data-estado="Rechazada">Rechazar</button>
      </div>
    `).join("");

    this.shadowRoot.querySelectorAll(".btn-estado").forEach(btn => {
      btn.addEventListener("click", async e => {
        const id = e.target.dataset.id;
        const estado = e.target.dataset.estado;
        await fetch(`http://127.0.0.1:5000/api/adopciones/${id}`, {
          method: "PUT",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({estado})
        });
        await this.loadSolicitudes(); // recarga después del cambio
      });
    });
  }
}

customElements.define("adopcion-list", AdopcionList);
