describe('Caso 1 - Ordenar productos por precio', () => {

  it('El usuario se loguea y ordena los productos de menor a mayor', function() {
    cy.visit('https://www.saucedemo.com/')
    cy.get('#user-name').type('standard_user')
    cy.get('#password').type('secret_sauce')
    cy.get('#login-button').click()

    // Ordenar por "Price (low to high)"
    cy.get('.product_sort_container').select('lohi')

    // Verificar que los precios estén ordenados de menor a mayor
    let precios = []
    cy.get('.inventory_item_price').each(($el) => {
      precios.push(parseFloat($el.text().replace('$', '')))
    }).then( function () {
      const preciosOrdenados = [...precios].sort((a, b) => a - b)
      expect(precios).to.deep.equal(preciosOrdenados)
    })
  })
})