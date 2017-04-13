# -*- coding: utf-8 -*-
from rest_framework import serializers


class BaseSerializable(serializers.ModelSerializer):
    # Initialize normally, but exclude/include fields dynamically
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        exclude = kwargs.pop('exclude', None)
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(BaseSerializable, self).__init__(*args, **kwargs)

        if fields is not None or exclude is not None:
            # Drop any fields that are not specified in the `fields` argument.
            excluded_fields = set()
            if fields is not None:
                allowed = set(fields)
                existing = set(self.fields.keys())
                excluded_fields = existing - allowed
            else:
                excluded_fields = set(exclude)

            for field_name in excluded_fields:
                self.fields.pop(field_name)

    class Meta:
        abstract = True
