from rest_framework import serializers

class ServiceNodeSerializer(serializers.Serializer):
    """
    Service details
    """
    service_code = serializers.SerializerMethodField('get_service_code')    
    attributes = serializers.SerializerMethodField('get_attributes')
    
    def get_service_code(self, obj):        
        return 'node'
    
    def get_attributes(self, obj):        
        return  {
                'code': 'layer',
                'description': _('layer_slug'),
                'datatype': 'string',
                'datatype_description': _('Specify the slug of the layer in which you want to insert the node'),
                'order': 1,
                'required': True,
                'variable' : True
            }         

    
    class Meta:
        fields = ('service_code', 'attributes')

