# Aplicativo de Detecção de Imagens

Bem-vindo ao Aplicativo de Detecção de Imagens! Este aplicativo de desktop permite que você faça reconhecimento e classificação de objetos usando Python.

## Instalação

Siga estes passos para instalar o Aplicativo de Detecção de Imagens:

1. **Clone o Repositório**: Clone ou baixe este repositório para sua máquina local.

   ```bash
   git clone https://github.com/Joaosamaia/Image-recognition
   ```

2. **Navegue até o Diretório**: Mova-se para o diretório do repositório clonado.

   ```bash
   cd Image-recognition
   ```

3. **Baixe os Arquivos YOLO**: Faça o download dos arquivos YOLO necessários (coco.names, yolov3.cfg e yolov3.weights) e coloque-os dentro do diretório do projeto.

4. **Instale o Aplicativo**: Instale o Aplicativo de Detecção de Imagens usando o arquivo setup.py.

   ```bash
   python setup.py install
   ```

## Uso

Para usar o Aplicativo de Detecção de Imagens, siga estes passos:

1. **Execute o Aplicativo**: Execute o aplicativo executando o seguinte comando no terminal:

   ```bash
   image-detection
   ```

2. **Escolha Imagem ou Vídeo**: Assim que a janela do aplicativo abrir, você poderá escolher processar uma imagem ou um vídeo. Clique no botão respectivo ("Selecionar Imagem" ou "Selecionar Vídeo") para escolher seu arquivo.

3. **Visualize os Resultados**: O aplicativo exibirá a imagem ou vídeo escolhido com caixas delimitadoras e rótulos ao redor dos objetos detectados.

4. **Interrompa o Vídeo (Se Aplicável)**: Se você escolher processar um arquivo de vídeo, poderá interromper o processamento do vídeo a qualquer momento clicando no botão "Parar Vídeo".

5. **Selecionar Outro**: Após processar uma imagem, você pode escolher outra imagem clicando no botão "Selecionar Outro".

6. **Feche o Aplicativo**: Feche a janela do aplicativo quando terminar clicando no botão de fechar ou fechando a janela.

---