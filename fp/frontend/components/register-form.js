export class RegisterForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });
    this.shadowRoot.innerHTML = `
      <form id="registerForm">
        <h2>Registro</h2>
        <input type="text" id="username" placeholder="Usuario" required><br>
        <input type="email" id="email" placeholder="Email" required><br>
        <input type="password" id="password" placeholder="Contraseña" required><br>
        <button type="submit">Registrar</button>
      </form>
    `;
  }

  connectedCallback() {
    this.shadowRoot.querySelector("#registerForm").addEventListener("submit", async (e) => {
      e.preventDefault();
      const username = this.shadowRoot.querySelector("#username").value;
      const email = this.shadowRoot.querySelector("#email").value;
      const password = this.shadowRoot.querySelector("#password").value;

      const res = await fetch("http://127.0.0.1:5000/api/users/register", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ username, email, password })
      });
      const data = await res.json();
      alert("Usuario registrado: " + data.username);
    });
  }
}

customElements.define("register-form", RegisterForm);
