from pydantic import BaseModel

from api.models import Widget


class WidgetInput(BaseModel):
    name: str
    description: str


class WidgetOutput(BaseModel):
    id: int
    name: str
    description: str


class WidgetService:

    @staticmethod
    def serialize(widget: Widget) -> WidgetOutput:
        return WidgetOutput(
            id=widget.id,
            name=widget.name,
            description=widget.description
        )
    
    @staticmethod
    def create(widget_input: WidgetInput) -> WidgetOutput:
        widget = Widget.objects.create(
            name=widget_input.name,
            description=widget_input.description
        )
        return WidgetService.serialize(widget)

    @staticmethod
    def read(id: int) -> WidgetOutput:
        widget = Widget.objects.get(id=id)
        return WidgetService.serialize(widget)

    @staticmethod
    def update(id: int, widget_input: WidgetInput) -> int:
        return Widget.objects.filter(id=id).update(
            name=widget_input.name,
            description=widget_input.description
        )

    @staticmethod
    def delete(id: int) -> None:
        return Widget.objects.filter(id=id).delete()
    
    @staticmethod
    def list() -> list[WidgetOutput]:
        widgets = Widget.objects.all()
        return [ WidgetService.serialize(widget) for widget in widgets ]
