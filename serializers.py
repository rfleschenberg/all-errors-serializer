# This class is currently not used, but I would like to keep it
# for future reference.
class AllErrorsSerializer(serializers.Serializer):  # pragma: no cover
    # Combine field errors and errors from validate()
    # so we can display them all at once.

    def is_valid(self, raise_exception=False):
        super().is_valid(raise_exception=False)

        try:
            self.validate(self.data)
        except serializers.ValidationError as e:
            self._errors['non_field_errors'] = e.detail

        if self._errors and raise_exception:
            raise serializers.ValidationError(self._errors)

        return not bool(self._errors)
