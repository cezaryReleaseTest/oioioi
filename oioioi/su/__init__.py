"""The SU app is used to change the current logged in user on-the-fly.

   In other to achieve that goal, the module introduces concept of *effective*
   and *real* user privileges known from Unix-like systems. The *effective*
   user is stored in ``request.user`` object, while the *real* in
   ``request.real_user``.

   On-the-fly means that current session variables are preserved while changing
   *effective* user, which may be also a pitfall if some code stores
   there data directly connected with current user scope.
"""
from django.contrib.auth.backends import ModelBackend
from django.utils.translation import ugettext_lazy as _


SU_UID_SESSION_KEY = 'su_effective_user_id'
SU_BACKEND_SESSION_KEY = 'su_effective_backend'

# Modify django default backend to meet our needs
ModelBackend.supports_authentication = True
ModelBackend.description = _("Password authentication")
