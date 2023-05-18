# Checkpoint 3: Processamento de Imagens com Arduino

Este repositório contém o código e os recursos necessários para o Checkpoint 3. Neste checkpoint, o desafio é criar um sistema que utilize visão computacional em Python e um Arduino para realizar a tarefa de acender um LED usando a propria mão!

## Descrição

Neste checkpoint, você encontrará os seguintes recursos:

- Código-fonte em Arduino arduino.txt.
- Código-fonte em Python controller.py
- Documentação detalhada e instruções de uso.

## Pré-requisitos

Antes de executar o código, é necessário instalar as seguintes bibliotecas:

1. OpenCV (cv2): Execute o seguinte comando no terminal:

```
pip install opencv-python
```

2. Mediapipe (mediapipe): Execute o seguinte comando no terminal:

```
pip install mediapipe
```

3. Serial (serial): Execute o seguinte comando no terminal:

```
pip install pyserial
```

## Passos para Configuração

Siga os passos abaixo para configurar o ambiente e executar o código:

1. Clone este repositório.
2. Instale as bibliotecas necessárias (veja as instruções na documentação).
3. Conecte o Arduino ao computador.
4. Compile e carregue o código no Arduino.
5. Execute o programa e observe o processamento de imagens em tempo real.

## Compile e carregue o código no Arduino utilizando arduino IDE.

Para carregar o arquivo Arduino na Arduino IDE, siga as etapas abaixo:

1. Abra a Arduino IDE em seu computador.

2. Conecte o Arduino ao computador através do cabo USB.

3. No menu da Arduino IDE, vá em "Arquivo" e selecione "Abrir".

4. Navegue até o local onde o arquivo Arduino (.ino) está armazenado em seu computador e selecione-o.

5. O código será aberto na Arduino IDE.

6. Verifique se a placa Arduino correta está selecionada no menu "Ferramentas" > "Placa". Escolha a placa correspondente ao seu modelo de Arduino.

7. Verifique também se a porta serial correta está selecionada no menu "Ferramentas" > "Porta". Selecione a porta que está conectada ao seu Arduino.

8. Clique no botão "Verificar" (ícone de "check") para verificar se não há erros de compilação no código.

9. Se não houver erros, clique no botão "Carregar" (ícone de "seta") para carregar o código no Arduino.

10. Aguarde enquanto o código é compilado e carregado no Arduino. O status da operação será exibido na parte inferior da Arduino IDE.

11. Uma vez que o carregamento esteja concluído, o código estará em execução no Arduino.

Certifique-se de que o Arduino esteja corretamente conectado ao computador e que todos os drivers necessários estejam instalados.

Essas instruções permitem que você carregue o código Arduino na sua placa, permitindo que você utilize o programa desejado no Arduino para realizar suas funcionalidades específicas. Certifique-se de seguir os passos cuidadosamente e verifique se a placa e a porta serial selecionadas estão corretas antes de realizar o carregamento.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.




