from ninja import NinjaAPI

from api.widgets import WidgetInput, WidgetOutput, WidgetService


api = NinjaAPI()


@api.get("/hello")
def hello(request):
    return {"message": "Hello, world!"}


@api.post('/widget', response=WidgetOutput)
def create_widget(request, input: WidgetInput):
    return WidgetService.create(input)


@api.get('/widget/{id}', response=WidgetOutput)
def read_widget(request, id: int):
    return WidgetService.read(id)


@api.put('/widget/{id}')
def update_widget(request, id: int, input: WidgetInput):
    WidgetService.update(id, input)
    return 204


@api.delete('/widget/{id}')
def delete_widget(request, id: int):
    WidgetService.delete(id)
    return 204


@api.get('/widgets', response=list[WidgetOutput])
def list_widgets(request):
    return WidgetService.list()
