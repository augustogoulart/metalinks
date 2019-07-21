// https://docs.cypress.io/api/introduction/api.html

describe("Home test", () => {
  const githubBlogURL = 'https://github.blog/';

  it("Home page shows 'Involved'", () => {
    cy.visit("/");
    cy.contains("span", "Involved");
  });

  it("Home page has links", () => {
    cy.visit("/");
    cy.contains("a", "https://github.com/augustogoulart/involved");
  });

  it("Home page has input field", () => {
    cy.visit("/");
    cy.get("form").should('exist')
  });

  it("Can submit link withing input field", () => {
    cy.get('input[name="link"]').type(githubBlogURL);
    cy.get('form').submit()

  });

  it("Submitted link displays on the screen", () => {
    cy.get('input[name="link"]').type(githubBlogURL);
    cy.get('form').submit();
    cy.contains("a", githubBlogURL)
  });

  it("Submitted link must display across sessions", () => {
    cy.get('input[name="link"]').type(githubBlogURL);
    cy.get('form').submit();
    cy.reload();
    cy.contains("a", githubBlogURL)
  })
});
