export class LoginForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });
    this.shadowRoot.innerHTML = `
      <form id="loginForm">
        <h2>Login</h2>
        <input type="email" id="email" placeholder="Email" required><br>
        <input type="password" id="password" placeholder="Contraseña" required><br>
        <button type="submit">Ingresar</button>
      </form>
      <div id="tokenBox">Token: (aún no logueado)</div>
    `;
  }

  connectedCallback() {
    this.shadowRoot.querySelector("#loginForm").addEventListener("submit", async (e) => {
      e.preventDefault();
      const email = this.shadowRoot.querySelector("#email").value;
      const password = this.shadowRoot.querySelector("#password").value;

      const res = await fetch("http://127.0.0.1:5000/api/users/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ email, password })
      });
      const data = await res.json();

      if (data.token) {
        localStorage.setItem("token", data.token); // 👉 guardamos el token
        this.shadowRoot.querySelector("#tokenBox").textContent = "Token: " + data.token;
        alert("Login exitoso!");
      } else {
        alert("Error: " + data.error);
      }
    });
  }
}

customElements.define("login-form", LoginForm);
