from django.views.generic import TemplateView


class ChatView(TemplateView):
    template_name = "chat/index.html"


class RoomView(TemplateView):

    template_name = "chat/room.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["room_name"] = self.kwargs['room_name']
        return data