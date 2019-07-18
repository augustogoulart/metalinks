// https://docs.cypress.io/api/introduction/api.html

describe("Home test", () => {
  const githubBlog = 'https://github.blog/';

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
    cy.get('form').within(($form) => {
      cy.get('input[name="link"]').type(githubBlog);
      cy.root().submit()
    });
  });

  it("Submited link displays on the screen", () => {
    cy.get('form').within(($form) => {
      cy.get('input[name="link"]').type(githubBlog);
      cy.root().submit()

    });
    cy.contains("a", "https://github.blog/")

  })
});
