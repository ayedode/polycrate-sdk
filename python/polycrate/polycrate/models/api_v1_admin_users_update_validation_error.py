from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_admin_users_update_email_error_component import ApiV1AdminUsersUpdateEmailErrorComponent
    from ..models.api_v1_admin_users_update_email_verified_error_component import (
        ApiV1AdminUsersUpdateEmailVerifiedErrorComponent,
    )
    from ..models.api_v1_admin_users_update_first_name_error_component import (
        ApiV1AdminUsersUpdateFirstNameErrorComponent,
    )
    from ..models.api_v1_admin_users_update_is_active_error_component import ApiV1AdminUsersUpdateIsActiveErrorComponent
    from ..models.api_v1_admin_users_update_is_billing_contact_error_component import (
        ApiV1AdminUsersUpdateIsBillingContactErrorComponent,
    )
    from ..models.api_v1_admin_users_update_is_maintenance_contact_error_component import (
        ApiV1AdminUsersUpdateIsMaintenanceContactErrorComponent,
    )
    from ..models.api_v1_admin_users_update_is_staff_error_component import ApiV1AdminUsersUpdateIsStaffErrorComponent
    from ..models.api_v1_admin_users_update_is_superuser_error_component import (
        ApiV1AdminUsersUpdateIsSuperuserErrorComponent,
    )
    from ..models.api_v1_admin_users_update_last_name_error_component import ApiV1AdminUsersUpdateLastNameErrorComponent
    from ..models.api_v1_admin_users_update_non_field_errors_error_component import (
        ApiV1AdminUsersUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_admin_users_update_role_error_component import ApiV1AdminUsersUpdateRoleErrorComponent


T = TypeVar("T", bound="ApiV1AdminUsersUpdateValidationError")


@_attrs_define
class ApiV1AdminUsersUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AdminUsersUpdateEmailErrorComponent | ApiV1AdminUsersUpdateEmailVerifiedErrorComponent |
            ApiV1AdminUsersUpdateFirstNameErrorComponent | ApiV1AdminUsersUpdateIsActiveErrorComponent |
            ApiV1AdminUsersUpdateIsBillingContactErrorComponent | ApiV1AdminUsersUpdateIsMaintenanceContactErrorComponent |
            ApiV1AdminUsersUpdateIsStaffErrorComponent | ApiV1AdminUsersUpdateIsSuperuserErrorComponent |
            ApiV1AdminUsersUpdateLastNameErrorComponent | ApiV1AdminUsersUpdateNonFieldErrorsErrorComponent |
            ApiV1AdminUsersUpdateRoleErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AdminUsersUpdateEmailErrorComponent
        | ApiV1AdminUsersUpdateEmailVerifiedErrorComponent
        | ApiV1AdminUsersUpdateFirstNameErrorComponent
        | ApiV1AdminUsersUpdateIsActiveErrorComponent
        | ApiV1AdminUsersUpdateIsBillingContactErrorComponent
        | ApiV1AdminUsersUpdateIsMaintenanceContactErrorComponent
        | ApiV1AdminUsersUpdateIsStaffErrorComponent
        | ApiV1AdminUsersUpdateIsSuperuserErrorComponent
        | ApiV1AdminUsersUpdateLastNameErrorComponent
        | ApiV1AdminUsersUpdateNonFieldErrorsErrorComponent
        | ApiV1AdminUsersUpdateRoleErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_admin_users_update_email_error_component import (
            ApiV1AdminUsersUpdateEmailErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_first_name_error_component import (
            ApiV1AdminUsersUpdateFirstNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_is_active_error_component import (
            ApiV1AdminUsersUpdateIsActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_is_billing_contact_error_component import (
            ApiV1AdminUsersUpdateIsBillingContactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_is_maintenance_contact_error_component import (
            ApiV1AdminUsersUpdateIsMaintenanceContactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_is_staff_error_component import (
            ApiV1AdminUsersUpdateIsStaffErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_is_superuser_error_component import (
            ApiV1AdminUsersUpdateIsSuperuserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_last_name_error_component import (
            ApiV1AdminUsersUpdateLastNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_non_field_errors_error_component import (
            ApiV1AdminUsersUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_role_error_component import (
            ApiV1AdminUsersUpdateRoleErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AdminUsersUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersUpdateEmailErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersUpdateFirstNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersUpdateLastNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersUpdateIsActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersUpdateIsStaffErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersUpdateIsSuperuserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersUpdateRoleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersUpdateIsMaintenanceContactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersUpdateIsBillingContactErrorComponent):
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
        from ..models.api_v1_admin_users_update_email_error_component import (
            ApiV1AdminUsersUpdateEmailErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_email_verified_error_component import (
            ApiV1AdminUsersUpdateEmailVerifiedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_first_name_error_component import (
            ApiV1AdminUsersUpdateFirstNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_is_active_error_component import (
            ApiV1AdminUsersUpdateIsActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_is_billing_contact_error_component import (
            ApiV1AdminUsersUpdateIsBillingContactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_is_maintenance_contact_error_component import (
            ApiV1AdminUsersUpdateIsMaintenanceContactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_is_staff_error_component import (
            ApiV1AdminUsersUpdateIsStaffErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_is_superuser_error_component import (
            ApiV1AdminUsersUpdateIsSuperuserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_last_name_error_component import (
            ApiV1AdminUsersUpdateLastNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_non_field_errors_error_component import (
            ApiV1AdminUsersUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_admin_users_update_role_error_component import (
            ApiV1AdminUsersUpdateRoleErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AdminUsersUpdateEmailErrorComponent
                | ApiV1AdminUsersUpdateEmailVerifiedErrorComponent
                | ApiV1AdminUsersUpdateFirstNameErrorComponent
                | ApiV1AdminUsersUpdateIsActiveErrorComponent
                | ApiV1AdminUsersUpdateIsBillingContactErrorComponent
                | ApiV1AdminUsersUpdateIsMaintenanceContactErrorComponent
                | ApiV1AdminUsersUpdateIsStaffErrorComponent
                | ApiV1AdminUsersUpdateIsSuperuserErrorComponent
                | ApiV1AdminUsersUpdateLastNameErrorComponent
                | ApiV1AdminUsersUpdateNonFieldErrorsErrorComponent
                | ApiV1AdminUsersUpdateRoleErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_update_error_type_0 = (
                        ApiV1AdminUsersUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_update_error_type_1 = (
                        ApiV1AdminUsersUpdateEmailErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_update_error_type_2 = (
                        ApiV1AdminUsersUpdateFirstNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_update_error_type_3 = (
                        ApiV1AdminUsersUpdateLastNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_update_error_type_4 = (
                        ApiV1AdminUsersUpdateIsActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_update_error_type_5 = (
                        ApiV1AdminUsersUpdateIsStaffErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_update_error_type_6 = (
                        ApiV1AdminUsersUpdateIsSuperuserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_update_error_type_7 = (
                        ApiV1AdminUsersUpdateRoleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_update_error_type_8 = (
                        ApiV1AdminUsersUpdateIsMaintenanceContactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_update_error_type_9 = (
                        ApiV1AdminUsersUpdateIsBillingContactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_admin_users_update_error_type_10 = (
                    ApiV1AdminUsersUpdateEmailVerifiedErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_admin_users_update_error_type_10

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_admin_users_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_admin_users_update_validation_error.additional_properties = d
        return api_v1_admin_users_update_validation_error

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
