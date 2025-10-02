export class UserTable extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });
    this.shadowRoot.innerHTML = `
      <h2>Usuarios registrados</h2>
      <button id="loadUsers">Cargar usuarios</button>
      <table>
        <thead>
          <tr>
            <th>ID</th><th>Usuario</th><th>Email</th><th>Rol</th>
          </tr>
        </thead>
        <tbody id="userTable"></tbody>
      </table>
    `;
  }

  connectedCallback() {
    this.shadowRoot.querySelector("#loadUsers").addEventListener("click", async () => {
      const res = await fetch("http://127.0.0.1:5000/api/users/");
      const data = await res.json();
      const table = this.shadowRoot.querySelector("#userTable");
      table.innerHTML = "";
      data.forEach(u => {
        table.innerHTML += `
          <tr>
            <td>${u.id}</td>
            <td>${u.username}</td>
            <td>${u.email}</td>
            <td>${u.role}</td>
          </tr>`;
      });
    });
  }
}

customElements.define("user-table", UserTable);
