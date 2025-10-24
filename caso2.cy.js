describe("Caso 2 - Validar errores en checkout", () => {

  it("Verificar errores de campos obligatorios", () => {
    cy.visit("/");
    cy.get("#user-name").type("standard_user");
    cy.get("#password").type("secret_sauce");
    cy.get("#login-button").click();

    // Agregar todos los productos
    cy.get(".btn_inventory").click({ multiple: true });

    // Ir al carrito
    cy.get(".shopping_cart_link").click();
    cy.get(".cart_item").should("have.length", 6);

    // Ir al checkout
    cy.get("#checkout").click();

    // Nombre vacío
    cy.get("#first-name").type("Ale");
    cy.get("#continue").click();
    cy.get("[data-test='error']").should("contain", "Error: Last Name is required");

    // Agregar apellido y volver a probar
    cy.get("#last-name").type("Rodriguez");
    cy.get("#continue").click();
    cy.get("[data-test='error']").should("contain", "Error: Postal Code is required");
  });

});