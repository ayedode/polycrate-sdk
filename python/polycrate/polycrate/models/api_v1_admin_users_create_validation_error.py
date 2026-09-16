from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_admin_users_create_email_error_component import ApiV1AdminUsersCreateEmailErrorComponent
    from ..models.api_v1_admin_users_create_email_verified_error_component import (
        ApiV1AdminUsersCreateEmailVerifiedErrorComponent,
    )
    from ..models.api_v1_admin_users_create_first_name_error_component import (
        ApiV1AdminUsersCreateFirstNameErrorComponent,
    )
    from ..models.api_v1_admin_users_create_is_active_error_component import ApiV1AdminUsersCreateIsActiveErrorComponent
    from ..models.api_v1_admin_users_create_is_billing_contact_error_component import (
        ApiV1AdminUsersCreateIsBillingContactErrorComponent,
    )
    from ..models.api_v1_admin_users_create_is_maintenance_contact_error_component import (
        ApiV1AdminUsersCreateIsMaintenanceContactErrorComponent,
    )
    from ..models.api_v1_admin_users_create_is_staff_error_component import ApiV1AdminUsersCreateIsStaffErrorComponent
    from ..models.api_v1_admin_users_create_is_superuser_error_component import (
        ApiV1AdminUsersCreateIsSuperuserErrorComponent,
    )
    from ..models.api_v1_admin_users_create_last_name_error_component import ApiV1AdminUsersCreateLastNameErrorComponent
    from ..models.api_v1_admin_users_create_non_field_errors_error_component import (
        ApiV1AdminUsersCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_admin_users_create_role_error_component import ApiV1AdminUsersCreateRoleErrorComponent


T = TypeVar("T", bound="ApiV1AdminUsersCreateValidationError")


@_attrs_define
class ApiV1AdminUsersCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AdminUsersCreateEmailErrorComponent | ApiV1AdminUsersCreateEmailVerifiedErrorComponent |
            ApiV1AdminUsersCreateFirstNameErrorComponent | ApiV1AdminUsersCreateIsActiveErrorComponent |
            ApiV1AdminUsersCreateIsBillingContactErrorComponent | ApiV1AdminUsersCreateIsMaintenanceContactErrorComponent |
            ApiV1AdminUsersCreateIsStaffErrorComponent | ApiV1AdminUsersCreateIsSuperuserErrorComponent |
            ApiV1AdminUsersCreateLastNameErrorComponent | ApiV1AdminUsersCreateNonFieldErrorsErrorComponent |
            ApiV1AdminUsersCreateRoleErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AdminUsersCreateEmailErrorComponent
        | ApiV1AdminUsersCreateEmailVerifiedErrorComponent
        | ApiV1AdminUsersCreateFirstNameErrorComponent
        | ApiV1AdminUsersCreateIsActiveErrorComponent
        | ApiV1AdminUsersCreateIsBillingContactErrorComponent
        | ApiV1AdminUsersCreateIsMaintenanceContactErrorComponent
        | ApiV1AdminUsersCreateIsStaffErrorComponent
        | ApiV1AdminUsersCreateIsSuperuserErrorComponent
        | ApiV1AdminUsersCreateLastNameErrorComponent
        | ApiV1AdminUsersCreateNonFieldErrorsErrorComponent
        | ApiV1AdminUsersCreateRoleErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_admin_users_create_email_error_component import (
            ApiV1AdminUsersCreateEmailErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_first_name_error_component import (
            ApiV1AdminUsersCreateFirstNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_is_active_error_component import (
            ApiV1AdminUsersCreateIsActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_is_billing_contact_error_component import (
            ApiV1AdminUsersCreateIsBillingContactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_is_maintenance_contact_error_component import (
            ApiV1AdminUsersCreateIsMaintenanceContactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_is_staff_error_component import (
            ApiV1AdminUsersCreateIsStaffErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_is_superuser_error_component import (
            ApiV1AdminUsersCreateIsSuperuserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_last_name_error_component import (
            ApiV1AdminUsersCreateLastNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_non_field_errors_error_component import (
            ApiV1AdminUsersCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_role_error_component import (
            ApiV1AdminUsersCreateRoleErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AdminUsersCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersCreateEmailErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersCreateFirstNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersCreateLastNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersCreateIsActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersCreateIsStaffErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersCreateIsSuperuserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersCreateRoleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersCreateIsMaintenanceContactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersCreateIsBillingContactErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_admin_users_create_email_error_component import (
            ApiV1AdminUsersCreateEmailErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_email_verified_error_component import (
            ApiV1AdminUsersCreateEmailVerifiedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_first_name_error_component import (
            ApiV1AdminUsersCreateFirstNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_is_active_error_component import (
            ApiV1AdminUsersCreateIsActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_is_billing_contact_error_component import (
            ApiV1AdminUsersCreateIsBillingContactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_is_maintenance_contact_error_component import (
            ApiV1AdminUsersCreateIsMaintenanceContactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_is_staff_error_component import (
            ApiV1AdminUsersCreateIsStaffErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_is_superuser_error_component import (
            ApiV1AdminUsersCreateIsSuperuserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_last_name_error_component import (
            ApiV1AdminUsersCreateLastNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_non_field_errors_error_component import (
            ApiV1AdminUsersCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_create_role_error_component import (
            ApiV1AdminUsersCreateRoleErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AdminUsersCreateEmailErrorComponent
                | ApiV1AdminUsersCreateEmailVerifiedErrorComponent
                | ApiV1AdminUsersCreateFirstNameErrorComponent
                | ApiV1AdminUsersCreateIsActiveErrorComponent
                | ApiV1AdminUsersCreateIsBillingContactErrorComponent
                | ApiV1AdminUsersCreateIsMaintenanceContactErrorComponent
                | ApiV1AdminUsersCreateIsStaffErrorComponent
                | ApiV1AdminUsersCreateIsSuperuserErrorComponent
                | ApiV1AdminUsersCreateLastNameErrorComponent
                | ApiV1AdminUsersCreateNonFieldErrorsErrorComponent
                | ApiV1AdminUsersCreateRoleErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_create_error_type_0 = (
                        ApiV1AdminUsersCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_create_error_type_1 = (
                        ApiV1AdminUsersCreateEmailErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_create_error_type_2 = (
                        ApiV1AdminUsersCreateFirstNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_create_error_type_3 = (
                        ApiV1AdminUsersCreateLastNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_create_error_type_4 = (
                        ApiV1AdminUsersCreateIsActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_create_error_type_5 = (
                        ApiV1AdminUsersCreateIsStaffErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_create_error_type_6 = (
                        ApiV1AdminUsersCreateIsSuperuserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_create_error_type_7 = (
                        ApiV1AdminUsersCreateRoleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_create_error_type_8 = (
                        ApiV1AdminUsersCreateIsMaintenanceContactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_create_error_type_9 = (
                        ApiV1AdminUsersCreateIsBillingContactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_admin_users_create_error_type_10 = (
                    ApiV1AdminUsersCreateEmailVerifiedErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_admin_users_create_error_type_10

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_admin_users_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_admin_users_create_validation_error.additional_properties = d
        return api_v1_admin_users_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
