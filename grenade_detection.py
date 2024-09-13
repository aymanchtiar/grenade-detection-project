import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
from ultralytics import YOLO

model = YOLO('model-2.pt')

class InterfaceScreen(Screen):
    def __init__(self, **kwargs):
        super(InterfaceScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        title = Label(text="Osiris Detection", font_size=40)
        subtitle = Label(text="A detection tool for hazardous objects in manufacturing environments", font_size=20)
        start_button = Button(text="Test the AI Model", font_size=24, size_hint=(1, 0.2))
        start_button.bind(on_release=self.go_to_detection)

        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(start_button)
        self.add_widget(layout)

    def go_to_detection(self, instance):
        self.manager.current = 'detection'


class DetectionScreen(Screen):
    def __init__(self, **kwargs):
        super(DetectionScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        self.image = Image()
        layout.add_widget(self.image)

        self.info_label = Label(text="No object detected", font_size=20)
        layout.add_widget(self.info_label)

        self.detection_count = 0

        self.add_widget(layout)

        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 30.0)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # Perform detection
            results = model(frame)
            detections = results[0]  
            high_confidence_boxes = []

            if len(detections.boxes) > 0:
                for detection in detections.boxes:
                    confidence = detection.conf.item()  
                    label = detection.cls.item() 

                    if confidence >= 0.5:
                        
                        high_confidence_boxes.append(detection)

                        label_name = model.names[int(label)] if model.names else str(label)
                        self.detection_count += 1
                        self.info_label.text = f"Detected: {label_name}, Confidence: {confidence:.2f}, Times Detected: {self.detection_count}"
                        break 
                else:
                    self.info_label.text = "No object detected with sufficient confidence"
            else:
                self.info_label.text = "No object detected"

           
            if high_confidence_boxes:
               
                frame = detections.plot(boxes=high_confidence_boxes)
            else:
                frame = results[0].orig_img

            buf1 = cv2.flip(frame, 0)
            buf = buf1.tobytes()  
            image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.image.texture = image_texture




    def on_leave(self, *args):
        self.capture.release()
        Clock.unschedule(self.update)


class OsirisApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InterfaceScreen(name='interface'))
        sm.add_widget(DetectionScreen(name='detection'))
        return sm


if __name__ == '__main__':
    OsirisApp().run()
