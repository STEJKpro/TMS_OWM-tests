from dataclasses import dataclass

@dataclass
class BaseElement:
    name: str
    locator: str
    
    
@dataclass
class ButtonElement:
    pass

@dataclass
class FieldElement:
    pass