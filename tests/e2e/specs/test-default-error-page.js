// https://docs.cypress.io/api/introduction/api.html

describe("Errors should use default error layout", () => {
  it("Error page has message", () => {
    cy.visit("/this-does-not-exist/");
    cy.contains("h1", "An error has occurred");
  });
});
