


    // Ao enviar o formulário
    document.getElementById('form-enderecos').addEventListener('submit', e => {
      e.preventDefault();
      const enderecos = Array.from(document.querySelectorAll('.endereco')).map(box => ({
        cep: box.querySelector('.cep').value,
        rua: box.querySelector('.rua').value,
        bairro: box.querySelector('.bairro').value,
        cidade: box.querySelector('.cidade').value,
        estado: box.querySelector('.estado').value,
        numero: box.querySelector('.numero').value
      }));
      
      console.log('Endereços cadastrados:', enderecos);
      alert(`${enderecos.length} endereço(s) salvos com sucesso!`);
    });
