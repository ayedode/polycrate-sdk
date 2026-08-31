from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_admin_users_partial_update_email_error_component import (
        ApiV1AdminUsersPartialUpdateEmailErrorComponent,
    )
    from ..models.api_v1_admin_users_partial_update_email_verified_error_component import (
        ApiV1AdminUsersPartialUpdateEmailVerifiedErrorComponent,
    )
    from ..models.api_v1_admin_users_partial_update_first_name_error_component import (
        ApiV1AdminUsersPartialUpdateFirstNameErrorComponent,
    )
    from ..models.api_v1_admin_users_partial_update_is_active_error_component import (
        ApiV1AdminUsersPartialUpdateIsActiveErrorComponent,
    )
    from ..models.api_v1_admin_users_partial_update_is_billing_contact_error_component import (
        ApiV1AdminUsersPartialUpdateIsBillingContactErrorComponent,
    )
    from ..models.api_v1_admin_users_partial_update_is_maintenance_contact_error_component import (
        ApiV1AdminUsersPartialUpdateIsMaintenanceContactErrorComponent,
    )
    from ..models.api_v1_admin_users_partial_update_is_staff_error_component import (
        ApiV1AdminUsersPartialUpdateIsStaffErrorComponent,
    )
    from ..models.api_v1_admin_users_partial_update_is_superuser_error_component import (
        ApiV1AdminUsersPartialUpdateIsSuperuserErrorComponent,
    )
    from ..models.api_v1_admin_users_partial_update_last_name_error_component import (
        ApiV1AdminUsersPartialUpdateLastNameErrorComponent,
    )
    from ..models.api_v1_admin_users_partial_update_non_field_errors_error_component import (
        ApiV1AdminUsersPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_admin_users_partial_update_role_error_component import (
        ApiV1AdminUsersPartialUpdateRoleErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AdminUsersPartialUpdateValidationError")


@_attrs_define
class ApiV1AdminUsersPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AdminUsersPartialUpdateEmailErrorComponent |
            ApiV1AdminUsersPartialUpdateEmailVerifiedErrorComponent | ApiV1AdminUsersPartialUpdateFirstNameErrorComponent |
            ApiV1AdminUsersPartialUpdateIsActiveErrorComponent | ApiV1AdminUsersPartialUpdateIsBillingContactErrorComponent
            | ApiV1AdminUsersPartialUpdateIsMaintenanceContactErrorComponent |
            ApiV1AdminUsersPartialUpdateIsStaffErrorComponent | ApiV1AdminUsersPartialUpdateIsSuperuserErrorComponent |
            ApiV1AdminUsersPartialUpdateLastNameErrorComponent | ApiV1AdminUsersPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1AdminUsersPartialUpdateRoleErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AdminUsersPartialUpdateEmailErrorComponent
        | ApiV1AdminUsersPartialUpdateEmailVerifiedErrorComponent
        | ApiV1AdminUsersPartialUpdateFirstNameErrorComponent
        | ApiV1AdminUsersPartialUpdateIsActiveErrorComponent
        | ApiV1AdminUsersPartialUpdateIsBillingContactErrorComponent
        | ApiV1AdminUsersPartialUpdateIsMaintenanceContactErrorComponent
        | ApiV1AdminUsersPartialUpdateIsStaffErrorComponent
        | ApiV1AdminUsersPartialUpdateIsSuperuserErrorComponent
        | ApiV1AdminUsersPartialUpdateLastNameErrorComponent
        | ApiV1AdminUsersPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1AdminUsersPartialUpdateRoleErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_admin_users_partial_update_email_error_component import (
            ApiV1AdminUsersPartialUpdateEmailErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_first_name_error_component import (
            ApiV1AdminUsersPartialUpdateFirstNameErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_is_active_error_component import (
            ApiV1AdminUsersPartialUpdateIsActiveErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_is_billing_contact_error_component import (
            ApiV1AdminUsersPartialUpdateIsBillingContactErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_is_maintenance_contact_error_component import (
            ApiV1AdminUsersPartialUpdateIsMaintenanceContactErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_is_staff_error_component import (
            ApiV1AdminUsersPartialUpdateIsStaffErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_is_superuser_error_component import (
            ApiV1AdminUsersPartialUpdateIsSuperuserErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_last_name_error_component import (
            ApiV1AdminUsersPartialUpdateLastNameErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_non_field_errors_error_component import (
            ApiV1AdminUsersPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_role_error_component import (
            ApiV1AdminUsersPartialUpdateRoleErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AdminUsersPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersPartialUpdateEmailErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersPartialUpdateFirstNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersPartialUpdateLastNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersPartialUpdateIsActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersPartialUpdateIsStaffErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersPartialUpdateIsSuperuserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersPartialUpdateRoleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersPartialUpdateIsMaintenanceContactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AdminUsersPartialUpdateIsBillingContactErrorComponent):
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
        from ..models.api_v1_admin_users_partial_update_email_error_component import (
            ApiV1AdminUsersPartialUpdateEmailErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_email_verified_error_component import (
            ApiV1AdminUsersPartialUpdateEmailVerifiedErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_first_name_error_component import (
            ApiV1AdminUsersPartialUpdateFirstNameErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_is_active_error_component import (
            ApiV1AdminUsersPartialUpdateIsActiveErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_is_billing_contact_error_component import (
            ApiV1AdminUsersPartialUpdateIsBillingContactErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_is_maintenance_contact_error_component import (
            ApiV1AdminUsersPartialUpdateIsMaintenanceContactErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_is_staff_error_component import (
            ApiV1AdminUsersPartialUpdateIsStaffErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_is_superuser_error_component import (
            ApiV1AdminUsersPartialUpdateIsSuperuserErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_last_name_error_component import (
            ApiV1AdminUsersPartialUpdateLastNameErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_non_field_errors_error_component import (
            ApiV1AdminUsersPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_admin_users_partial_update_role_error_component import (
            ApiV1AdminUsersPartialUpdateRoleErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AdminUsersPartialUpdateEmailErrorComponent
                | ApiV1AdminUsersPartialUpdateEmailVerifiedErrorComponent
                | ApiV1AdminUsersPartialUpdateFirstNameErrorComponent
                | ApiV1AdminUsersPartialUpdateIsActiveErrorComponent
                | ApiV1AdminUsersPartialUpdateIsBillingContactErrorComponent
                | ApiV1AdminUsersPartialUpdateIsMaintenanceContactErrorComponent
                | ApiV1AdminUsersPartialUpdateIsStaffErrorComponent
                | ApiV1AdminUsersPartialUpdateIsSuperuserErrorComponent
                | ApiV1AdminUsersPartialUpdateLastNameErrorComponent
                | ApiV1AdminUsersPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1AdminUsersPartialUpdateRoleErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_partial_update_error_type_0 = (
                        ApiV1AdminUsersPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_partial_update_error_type_1 = (
                        ApiV1AdminUsersPartialUpdateEmailErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_partial_update_error_type_2 = (
                        ApiV1AdminUsersPartialUpdateFirstNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_partial_update_error_type_3 = (
                        ApiV1AdminUsersPartialUpdateLastNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_partial_update_error_type_4 = (
                        ApiV1AdminUsersPartialUpdateIsActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_partial_update_error_type_5 = (
                        ApiV1AdminUsersPartialUpdateIsStaffErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_partial_update_error_type_6 = (
                        ApiV1AdminUsersPartialUpdateIsSuperuserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_partial_update_error_type_7 = (
                        ApiV1AdminUsersPartialUpdateRoleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_partial_update_error_type_8 = (
                        ApiV1AdminUsersPartialUpdateIsMaintenanceContactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_admin_users_partial_update_error_type_9 = (
                        ApiV1AdminUsersPartialUpdateIsBillingContactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_admin_users_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_admin_users_partial_update_error_type_10 = (
                    ApiV1AdminUsersPartialUpdateEmailVerifiedErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_admin_users_partial_update_error_type_10

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_admin_users_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_admin_users_partial_update_validation_error.additional_properties = d
        return api_v1_admin_users_partial_update_validation_error

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
