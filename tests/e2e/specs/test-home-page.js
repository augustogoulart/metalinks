// https://docs.cypress.io/api/introduction/api.html

describe("Home test", () => {
  it("Home page shows 'Involved'", () => {
    cy.visit("/");
    cy.contains("span", "Involved");
  });

  it("Home page has links", () => {
    cy.visit("/");
    cy.contains("a", "https://github.com/augustogoulart/involved");
  });

  it("Home page has input form", () => {
    cy.visit("/");
    cy.get("form").should('exist')
  })
});
