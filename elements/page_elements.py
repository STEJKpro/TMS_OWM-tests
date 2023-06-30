from dataclasses import dataclass, field

@dataclass
class BaseElement:
    name: str
    locator: str
    _element_type='BaseElement'
    
    @property
    def element_discription(self) -> str:
        return f'Название: {self.name};' \
            + f'\nLocator: {self.locator};'
    @property
    def type(self):
        return self._element_type
@dataclass
class ButtonElement(BaseElement):
    button_text:str
    _element_type='Button'

    @property
    def element_discription(self) -> str:
        return +f'Название: {self.name};' \
            + f'\nLocator: {self.locator};'\
            + f"\nТип: Кнопка"

@dataclass
class FieldElement(BaseElement):
    placeholder:str = field(default=None)
    _element_type='Field'
    
    @property
    def element_discription(self) -> str:
        return f'Название: {self.name};' \
            + f'\nLocator: {self.locator};' \
            + (f'\nPlaceholder: {self.placeholder};' if self.placeholder else '' )\
            + f"\nТип: Поле"

@dataclass
class CheckBoxElement(BaseElement):
    lable:str = field(default=None)
    checked:bool =field(default=False) # True - флаг установлен; False - флаг снят
    _element_type='CheckBox'
    
    @property
    def element_discription(self) -> str:
        return f'Название: {self.name};' \
            + f'\nLocator: {self.locator};' \
            + (f'\nLable: {self.lable};' if self.lable else '' )\
            + f"\nТип: CheckBox"

    def change_flag(self) -> None:
        """Метод изменеят сосотояние элемента
        True - флаг установлен
        False - флаг снят
        """
        self.checked = not self.checked
        
        
        
