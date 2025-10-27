 const container = document.getElementById('enderecos-container');
    const addBtn = document.getElementById('add-endereco');
    let count = 1;

    // Função para adicionar novo endereço
    addBtn.addEventListener('click', () => {
      count++;
      const novo = document.createElement('div');
      novo.classList.add('endereco');
      novo.dataset.index = count;
      novo.innerHTML = `
        <h3>Endereço ${count}</h3>
        <label>CEP:</label>
        <input type="text" name="cep" class="cep">

        <label>Rua:</label>
        <input type="text" name="rua" class="rua">

        <label>Bairro:</label>
        <input type="text" name="bairro" class="bairro">

        <label>Cidade:</label>
        <input type="text" name="cidade" class="cidade">

        <label>Estado:</label>
        <input type="text" name="estado" class="estado">

        <label>Número:</label>
        <input type="text" name="numero" class="numero">
      `;
      container.appendChild(novo);
      aplicarEventosCep();
    });