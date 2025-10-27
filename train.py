from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/detect/train3/weights/best.pt')
    '''model.train(
                data='Dataset/data.yaml',
                epochs=100,
                imgsz=640,
                batch=8,
                device=0
                ) '''
    
    model.predict('potholes.mp4', show=True)