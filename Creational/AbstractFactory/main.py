from abc import ABC, abstractmethod

# Abstract class for components
class Button(ABC):

    @abstractmethod
    def render(self):
        pass

class TextBox(ABC):
    
    @abstractmethod
    def render(self):
        pass

# Windows Concrete class
class WindowsButton(Button):
    
    def render(self):
        print("Windows Button!!")

class WindowsTextBox(TextBox):
    
    def render(self):
        print("Windows TextBox!!")

# Mac concrete class
class MacButton(Button):
    
    def render(self):
        print("Mac Button!!")

class MacTextBox(TextBox):
    
    def render(self):
        print("Mac TextBox!!")

# Abstract factory
class UIFactory(ABC):

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_textbox(self) -> TextBox:
        pass

# Windows concrete factory class
class WindowsFactory(UIFactory):

    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_textbox(self) -> TextBox:
        return WindowsTextBox()

# Mac concrete factory class
class MacFactory(UIFactory):

    def create_button(self) -> Button:
        return MacButton()
    
    def create_textbox(self) -> TextBox:
        return MacTextBox()

def render_ui(factory: UIFactory):
    button = factory.create_button()
    textbox = factory.create_textbox()
    button.render()
    textbox.render()

if __name__ == "__main__":
    os = input("Choose os (Windows/Mac): ").lower()
    factory = None
    if os == "windows":
        factory = WindowsFactory()
    elif os == "mac":
        factory = MacFactory()
    else:
        raise ValueError("Unsupported OS type")
    render_ui(factory)