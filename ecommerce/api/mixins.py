from .permissions import IsVendor, IsCustomer, IsAdmin
from rest_framework.permissions import IsAuthenticated
class VendorPermissionMixin(object):
    permission_classes = [IsAuthenticated, IsVendor]
class CustomerPermissionMixin(object):
    permission_classes = [IsAuthenticated, IsCustomer]