import os
import cv2
import numpy as np
import tkinter as tk
from tkinter import Button, filedialog
from PIL import Image, ImageTk

# Carregando os arquivos do modelo YOLO como variaveis
yolo_weights = 'yolov3.weights'
yolo_config = 'yolov3.cfg'
coco_names = 'coco.names'

# Carregando o diretorio atual como variavel
project_dir = os.path.abspath(os.path.dirname(__file__))

# Funcao para retornar a tela principal e redefinir os botoes
def return_main_screen():
    global cap, is_running
    if cap is not None:
        cap.release()
    is_running = False
    panel.config(image='')
    btn_choose_image.config(text="Escolha uma imagem", command=process_image, bg="blue", highlightbackground="red")
    btn_choose_video.config(text="Escolha um video", command=process_video, bg="blue", highlightbackground="red")

# Funcao para redimensionar uma imagem mantendo sua proporcao
def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dimensions = None
    (h, w) = image.shape[:2]

    # Retorna a imagem original se nenhuma dimensao for fornecida
    if width is None and height is None:
        return image
    # Calcula a proporcao para redimensionar altura e largura
    if width is None:
        r = height / float(h)
        dimensions = (int(w * r), height)
    else:
        r = width / float(h)
        dimensions = (width, int(h * r))

    # Redimensiona a imagem
    resized = cv2.resize(image, dimensions, interpolation=inter)
    return resized

# Funcao para processar um arquivo de imagem e exibir classificacoes
def process_image():
    global panel, net, classes
    image_file = filedialog.askopenfilename(initialdir=project_dir, title="Escolha uma imagem",
                                            filetypes=(("Image Files", "*.jpg;*.jpeg;*.png"), ("All Files", "*.*")))
    if image_file:
        frame = cv2.imread(image_file)
        if frame is not None:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = resize(frame, width=view_square_width, height=view_square_height)

            (H, W) = frame.shape[:2]
            blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
            net.setInput(blob)
            ln = net.getLayerNames()
            ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]
            layer_outputs = net.forward(ln)

            boxes = []
            confidences = []
            class_ids = []

            # Processa as classificacoes das camadas de saida YOLO
            for output in layer_outputs:
                for detection in output:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]

                    # Filtra classificacoes fracas (de baixa acuracia)
                    if confidence > 0.5:
                        box = detection[0:4] * np.array([W, H, W, H])
                        (centerX, centerY, width, height) = box.astype("int")

                        x = int(centerX - (width / 2))
                        y = int(centerY - (height / 2))

                        boxes.append([x, y, int(width), int(height)])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            # Aplica supressao de nao-maxima para evitar caixas sobrepostas (filtro de Canny)
            idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

            # Desenha as caixas delimitadoras e seus rotulos na imagem
            if len(idxs) > 0:
                for i in idxs.flatten():
                    (x, y) = (boxes[i][0], boxes[i][1])
                    (w, h) = (boxes[i][2], boxes[i][3])

                    color = [int(c) for c in np.random.randint(0, 255, size=(3,))]
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                    text = "{}: {:.4f}".format(classes[class_ids[i]], confidences[i])
                    cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=img)
            panel.config(image=img)
            panel.image = img

            btn_choose_image.config(text="Escolha outra imagem", command=process_image, bg="blue", highlightbackground="red")

#  Funcao para processar um arquivo de video e exibir classificacoes
def process_video():
    global cap, is_running
    video_file = filedialog.askopenfilename(initialdir=project_dir, title="Escolha um video",
                                            filetypes=(("Video Files", "*.mp4;*.avi;*.mov"), ("All Files", "*.*")))
    if video_file:
        cap = cv2.VideoCapture(video_file)
        btn_choose_video.config(text="Parar Video", command=stop_video, bg="blue", highlightbackground="red")
        is_running = True
        
        # Funcao para atualizar o video frame a frame
        def update_camera():
            global cap, panel, net, classes, is_running
            if is_running and cap is not None:
                ret, frame = cap.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = resize(frame, width=view_square_width, height=view_square_height)

                    (H, W) = frame.shape[:2]
                    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
                    net.setInput(blob)
                    ln = net.getLayerNames()
                    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]
                    layer_outputs = net.forward(ln)

                    boxes = []
                    confidences = []
                    class_ids = []

                    # Processa as classificacoes das camadas de saida YOLO
                    for output in layer_outputs:
                        for detection in output:
                            scores = detection[5:]
                            class_id = np.argmax(scores)
                            confidence = scores[class_id]

                            # Filter out weak detections
                            if confidence > 0.5:
                                box = detection[0:4] * np.array([W, H, W, H])
                                (centerX, centerY, width, height) = box.astype("int")

                                x = int(centerX - (width / 2))
                                y = int(centerY - (height / 2))

                                boxes.append([x, y, int(width), int(height)])
                                confidences.append(float(confidence))
                                class_ids.append(class_id)

                    # Aplica supressao de nao-maxima para evitar caixas sobrepostas (filtro de Canny)
                    idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

                    # Desenha as caixas delimitadoras e seus rotulos no frame do video
                    if len(idxs) > 0:
                        for i in idxs.flatten():
                            (x, y) = (boxes[i][0], boxes[i][1])
                            (w, h) = (boxes[i][2], boxes[i][3])

                            color = [int(c) for c in np.random.randint(0, 255, size=(3,))]
                            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                            text = "{}: {:.4f}".format(classes[class_ids[i]], confidences[i])
                            cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                    # Converte o frame processado para um formato compativel com o Tkinter
                    img = Image.fromarray(frame)
                    img = ImageTk.PhotoImage(image=img)
                    panel.config(image=img)
                    panel.image = img
            # Se o video ainda estiver rolando, agenda a proxima atualizacao de frame apos 5ms
            if is_running:
                panel.after(5, update_camera)
        
        update_camera()
    else:
        cap = None
        return

# Funcao para interromper o processamento de video
def stop_video():
    global cap, is_running
    if cap is not None:
        cap.release()
    is_running = False
    panel.config(image='')
    btn_choose_video.config(text="Escolha um video", command=process_video, bg="blue", highlightbackground="red")

# Carregando os rotulos de classe da COCO
with open(coco_names, 'r') as f:
    classes = f.read().strip().split('\n')

# Carregando a rede YOLO
net = cv2.dnn.readNetFromDarknet(yolo_config, yolo_weights)

# Funcao para criar a janela inicial com componentes GUI
def create_initial_window():
    global root, panel, btn_choose_image, btn_choose_video, view_square_width, view_square_height, cap, is_running

    # Cria a janela principal do Tkinter
    root = tk.Tk()
    root.title("Image recognition")
    root.geometry("1280x720")
    root.configure(bg='gray')

    # Definindo o espaco para conter os botoes
    button_frame = tk.Frame(root, bg='gray')
    button_frame.pack(side=tk.TOP, pady=20)

    # Botao para escolher uma imagem
    btn_choose_image = Button(button_frame, text="Escolha uma imagem", command=process_image, bg="blue", highlightbackground="red", highlightthickness=2)
    btn_choose_image.pack(side=tk.LEFT, padx=10)

    # Botao para escolher um video
    btn_choose_video = Button(button_frame, text="Escolha um video", command=process_video, bg="blue", highlightbackground="red", highlightthickness=2)
    btn_choose_video.pack(side=tk.LEFT, padx=10)

    # Definindo as dimensões da area de visualizacao de midia
    view_square_width = 720
    view_square_height = 500

    # Definindo o espaco para conter a area de visualizacao de midia
    view_square = tk.Frame(root, width=view_square_width, height=view_square_height, bg='gray', highlightbackground="white", highlightthickness=5)
    view_square.pack(side=tk.BOTTOM, pady=20)

    # Label pra exibir imagens ou frames de video
    panel = tk.Label(view_square)
    panel.pack()

    # Inicializando as variaveis
    is_running = False
    cap = None

    # Iniciando o loop de eventos do Tkinter
    root.mainloop()

create_initial_window()