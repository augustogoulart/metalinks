// https://docs.cypress.io/api/introduction/api.html

describe("Home test", () => {
  it("Home page shows 'Involved'", () => {
    cy.visit("/");
    cy.contains("h1", "Involved");
  });

  it("Home has links", () => {
    cy.visit("/");
    cy.contains("a", "This is a link");
  })
});
