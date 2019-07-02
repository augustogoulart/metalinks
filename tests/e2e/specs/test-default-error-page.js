// https://docs.cypress.io/api/introduction/api.html

describe("Errors should use default error layout", () => {
  it("Error page has message", () => {
    cy.visit({url: "/this-does-not-exist/", failOnStatusCode: false});
    cy.contains("h1", "An error has occurred");
  });
});
