from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class ExtraCommonPasswordValidator:
    extra_common_passwords = {
        "123456789",
        "password123",
        "abc12345",
        "bangladesh",
        "innovative123",
        "iloveyou",
    }

    def validate(self, password, user=None):
        if password.lower() in self.extra_common_passwords:
            raise ValidationError(
                _("This password is too common."),
                code="password_too_common",
            )

    def get_help_text(self):
        return _("Your password cannot be a commonly used password.")
