# Aplicativo de Detecção de Imagens

Bem-vindo ao Aplicativo de Detecção de Imagens! Este aplicativo de desktop construido com Tkinter utiliza a rede YOLO (You Only Look Once) que permite que você faça reconhecimento e classificação de objetos usando Python.

## Instalação

Siga estes passos para instalar o Aplicativo de Detecção de Imagens:


1. **Instale o Python 3.10+**: Se você ainda não tiver o Python 3.10+ instalado, siga as instruções adequadas para seu sistema operacional e faça download no [site oficial do Python](https://www.python.org/downloads/).

2. **Clone o Repositório**: No terminal(cmd), clone ou baixe este repositório para sua máquina local.

   ```bash
   git clone https://github.com/Joaosamaia/Image-recognition
   ```

3. **Navegue até o Diretório**: No terminal(cmd), mova-se para o diretório do repositório clonado.

   ```bash
   cd Image-recognition
   ```

4. **Baixe os Arquivos YOLO**:
    - [COCO Names](https://github.com/pjreddie/darknet/blob/master/data/coco.names)
    - [YOLOv3 Weights](https://pjreddie.com/media/files/yolov3.weights)
    - [YOLOv3 Config](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
         
    e coloque-os dentro do diretório do projeto.
   

5. **Instale o Aplicativo**: No terminal(cmd), instale o Aplicativo de Detecção de Imagens usando o arquivo setup.py.

   ```bash
   pip install setuptools //instale a dependencia caso nao ha possua

   python setup.py install
   ```
6. **Organize o diretório do projeto**: Confirme que a o diretório do projeto está organizado de maneira correta, conforme o exemplo abaixo.
   ```plaintext
   ..\
   ├── coco.names
   ├── yolov3.weights
   ├── yolov3.cfg
   ├── app.py
   ├── setup.py
   ├── .gitignore
   └── README.md
   ```

## Uso

Para usar o Aplicativo de Detecção de Imagens, siga estes passos:

1. **Execute o Aplicativo**: 

      No terminal(cmd), execute o aplicativo executando o seguinte comando:
   ```bash
   image-detection
   ```
      Ou execute o arquivo app.py diretamente:

   ```bash
   python app.py
   ```
      Se certifique de ter as dependecias necessarias instaladas ^-^ (caso nao as tenha, use o comando abaixo)
   ```bash
   pip install opencv-python-headless numpy pillow
   ```

2. **Escolha Imagem ou Vídeo**: Assim que a janela do aplicativo abrir, você poderá escolher processar uma imagem ou um vídeo. Clique no botão respectivo ("Selecionar Imagem" ou "Selecionar Vídeo") para escolher seu arquivo de mídia.

3. **Visualize os Resultados**: O aplicativo exibirá a imagem ou vídeo escolhido com caixas delimitadoras e rótulos ao redor dos objetos detectados.

4. **Interrompa o Vídeo (Se tiver escolhido um video)**: Se você escolher processar um arquivo de vídeo, poderá interromper o processamento do vídeo a qualquer momento clicando no botão "Parar Vídeo".

5. **Selecionar Outro (Se tiver escolhido uma imagem)**: Após processar uma imagem, você pode escolher outra imagem clicando no botão "Selecionar Outro".

6. **Continue testando!**: Clique no botão respectivo ("Selecionar Imagem" ou "Selecionar Vídeo") para escolher um novo arquivo de mídia.

7. **Feche o Aplicativo**: Feche a janela do aplicativo quando terminar clicando no botão de fechar ou fechando a janela.

---
