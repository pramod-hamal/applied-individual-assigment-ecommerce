from rest_framework import renderers

class CoreApiResponse(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context:
            response = renderer_context['response']
            if response.exception:
                data = {
                    'status': 'error',
                    'message': data
                }
            else:
                data = {
                    'status': 'success',
                    'data': data
                }
        return super(CoreApiResponse, self).render(data, accepted_media_type, renderer_context)