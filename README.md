# AuctionProject
Este repositório é um projeto acadêmico focado na integração de conceitos de banco de dados, desenvolvimento web front-end e back-end, e design, utilizando tecnologias como HTML, CSS, Python, JavaScript e MariaDB, que serão usadas para desenvolver um site fictício de leilões.

## Sumário

## Arquitetura do Projeto

## Modelos

## Notificação

- ### Envio ```/myapp/services/routes```
  A função ```send_email(email, subject ,content)``` recebe como parâmetros o e-mail do usuário, o assunto e o conteúdo da mensagem, e envia para o usuário. O gerenciamento de notificações é feito por...

## Asaas
- ### Cliente ```/services/CreateAsaasCustomer```
  Para realizar pagamentos, é necessário criar um cliente dentro da API de pagamentos Asaas. A função ```create_asaas_customer(id_user)``` cria um cliente no servidor da Asaas e o adiciona ao banco de dados.
  
  Ela retorna o código de status e a descrição, e recebe o ID do usuário que ganhará o id_asaas como parâmetro.
  
- ### Link de pagamento
  em desenvolvimento 
- ### Webhook ```/routes/actions/Webhook```
  Sempre que ocorre alguma alteração em qualquer processo de pagamento, essa rota recebe as informações sobre o movimento do processo a partir da API de pagamento.
Por motivos de segurança, essa rota recebe uma chave (senha) no cabeçalho para garantir que apenas usuários autorizados possam realizar movimentações.
  
 Essa função opera através da rota ```"/payment/webhook"``` e recebe um POST JSON com informações, incluindo a mais importante, ```"EVENT"```, que contém o código do evento.
Abaixo estão os possíveis códigos que podem ser recebidos:

  ```PAYMENT_AUTHORIZED```
    - Pagamento com cartão autorizado e aguardando captura.

    ```PAYMENT_APPROVED_BY_RISK_ANALYSIS```
    - Pagamento com cartão aprovado por análise manual de risco.

    ```PAYMENT_CREATED```
    - Geração de uma nova cobrança.

    ```PAYMENT_CONFIRMED```
    - Cobrança confirmada (pagamento efetuado, mas saldo ainda não disponível).

    ```PAYMENT_ANTICIPATED```
    - Pagamento antecipado.

    ```PAYMENT_DELETED```
    - Cobrança removida.

    ```PAYMENT_REFUNDED```
    - Cobrança estornada.

    ```PAYMENT_REFUND_DENIED```
    - Estorno negado.

    ```PAYMENT_CHARGEBACK_REQUESTED```
    - Chargeback recebido.

    ```PAYMENT_AWAITING_CHARGEBACK_REVERSAL```
    - Disputa ganha, aguardando transferência da adquirente.

    ```PAYMENT_DUNNING_REQUESTED```
    - Solicitação de negativação.

    ```PAYMENT_CHECKOUT_VIEWED```
    - Fatura visualizada pelo cliente.

    ```PAYMENT_PARTIALLY_REFUNDED```
    - Cobrança parcialmente estornada.

    ```PAYMENT_SPLIT_DIVERGENCE_BLOCK```
    - Valor bloqueado devido a divergência de divisão (split).

    ```PAYMENT_AWAITING_RISK_ANALYSIS```
    - Pagamento aguardando aprovação manual de risco.

    ```PAYMENT_REPROVED_BY_RISK_ANALYSIS```
    - Pagamento reprovado pela análise de risco.

    ```PAYMENT_UPDATED```
    - Alteração na data de vencimento ou no valor da cobrança.

    ```PAYMENT_RECEIVED```
    - Cobrança recebida.

    ```PAYMENT_OVERDUE```
    - Cobrança vencida.

    ```PAYMENT_RESTORED```
    - Pagamento restaurado.

    ```PAYMENT_REFUND_IN_PROGRESS```
    - Estorno em andamento (liquidação já agendada, estorno será realizado após execução).

    ```PAYMENT_RECEIVED_IN_CASH_UNDONE```
    - Recebimento em dinheiro desfeito.

    ```PAYMENT_CHARGEBACK_DISPUTE```
    - Em disputa de chargeback (documentos apresentados para contestação).

    ```PAYMENT_DUNNING_RECEIVED```
    - Recebimento de negativação.

    ```PAYMENT_BANK_SLIP_VIEWED```
    - Boleto visualizado pelo cliente.

    ```PAYMENT_CREDIT_CARD_CAPTURE_REFUSED```
    - Captura do cartão recusada.

    ```PAYMENT_SPLIT_CANCELLED```
    - Cobrança teve o split cancelado.

    ```PAYMENT_SPLIT_DIVERGENCE_BLOCK_FINISHED```
    - Bloqueio devido a divergência de split finalizado.

## Socket
- ### Join Room ```/sockets/Room```
    Sempre que um usuário entra em um leilão, todos os participantes desse leilão devem ser notificados.

    Essa notificação será enviada via Socket.IO, usando o evento ```"join_room"```

    Quando um usuário se conecta ao leilão, o servidor enviará uma mensagem para todos os clientes:

    No evento ```"server_content"```

    E especificamente na sala correspondente ao leilão que o usuário entrou.

    Assim, o frontend poderá exibir informações atualizadas em tempo real.

    O único parâmetro necessário é o ID do leilão, que estará em um JSON.

    O retorno será um JSON:
    ```js
    {
        type: "entry",
        room_id: INT,
        user_id: INT
        username: STR
        product_id: INT
        product_name: STR
    }
    ```

    Exemplo em JavaScript:
    ```html
      <script src="/socket.io/socket.io.js"></script>
      <script>

        const socket = io();

        function joinAuctionRoom(id_auction) {
          socket.emit("join_room", {
            id_auction = id_auction
          });
        }

        socket.on("server_content", (data) => {
          const response = data.response;
          if (response.type === "entry") {
            alert(`usr: ${response.username} \n room: ${response.room_id}`);
          }
        });

      </script>
    ```

- ### Lance ```/socket/Room```
  Sempre que um usuário fizer um lance em um leilão, todos os participantes deverão ser notificados.

  Essa notificação será enviada via Socket.IO, usando o evento ```"bid_content"``` 

  Quando um usuário fizer um lance, o servidor enviará uma mensagem para todos os clientes:

  No evento ```"server_content"```

  E especificamente na sala correspondente ao leilão em que o lance foi feito.

  Assim, o frontend poderá exibir as informações atualizadas em tempo real.

  Os parâmetros necessários são: ID do leilão, ID do usuário que fez o lance e valor do lance, que estarão em um JSON.

  Retorno esperado (JSON):
    ```js
    {
        type: "bid",
        room_id: INT,
        user_id: INT,
        username: STR,
        value: FLT/DBL,
        product_id: INT,
        product_name: STR
    }
    ```
  Exemplo em JavaScript:
  ```html
      <script src="/socket.io/socket.io.js"></script>
      <script>

        const socket = io();

        function sendBid(id_auction, id_user, value) {
          socket.emit("bid_content", {
            id_auction = id_auction,
            id_user = id_user,
            value = value
          });
        }

        socket.on("server_content", (data) => {
          const response = data.response;
          if (response.type === "bid") {
            alert(`usr: ${response.username} \n room: ${response.room_id}\n val: ${response.value}`);
          }
        });

      </script>
    ```
  

- ### Fechar leilão ```/sockets/CloseRoom```
  Sempre que um leilão é criado, ele possui um tempo limite predefinido para encerrar.
No entanto, pode acontecer de um usuário dar um lance no último minuto.
Por isso, sempre que um lance for feito nos últimos 2 minutos, o tempo é reiniciado para 2 minutos.

  A função ```close_auction(id_auction)``` remove todos os participantes da sala do socket, deleta o leilão e altera seu status.

  Para controlar o tempo, existe a função ```start_auction_timer(auction_id, seconds)```, que chama a funçãoon ```close_auction()``` após o tempo acabar. Caso um lance seja feito nos minutos finais, a função ```add_time_to_action(id_auction, seconds)``` will be called. é chamada. Em casos extremos ou exceções — por exemplo, uma queda do servidor — a função ```start()``` deve ser chamada, reiniciando o temporizador de todos os leilões registrados no banco de dados.

## Configuração e Implantação

## Segurança

## A Equipe
