from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_idp_identityproviders_list_created_by_users_error_component import (
        ApiV1IdpIdentityprovidersListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_list_kind_error_component import (
        ApiV1IdpIdentityprovidersListKindErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_list_name_exact_error_component import (
        ApiV1IdpIdentityprovidersListNameExactErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_list_organizations_error_component import (
        ApiV1IdpIdentityprovidersListOrganizationsErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_list_search_error_component import (
        ApiV1IdpIdentityprovidersListSearchErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_list_state_error_component import (
        ApiV1IdpIdentityprovidersListStateErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_list_state_not_error_component import (
        ApiV1IdpIdentityprovidersListStateNotErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_list_sync_mode_error_component import (
        ApiV1IdpIdentityprovidersListSyncModeErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_list_time_range_error_component import (
        ApiV1IdpIdentityprovidersListTimeRangeErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_list_workspaces_error_component import (
        ApiV1IdpIdentityprovidersListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1IdpIdentityprovidersListValidationError")


@_attrs_define
class ApiV1IdpIdentityprovidersListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1IdpIdentityprovidersListCreatedByUsersErrorComponent |
            ApiV1IdpIdentityprovidersListKindErrorComponent | ApiV1IdpIdentityprovidersListNameExactErrorComponent |
            ApiV1IdpIdentityprovidersListOrganizationsErrorComponent | ApiV1IdpIdentityprovidersListSearchErrorComponent |
            ApiV1IdpIdentityprovidersListStateErrorComponent | ApiV1IdpIdentityprovidersListStateNotErrorComponent |
            ApiV1IdpIdentityprovidersListSyncModeErrorComponent | ApiV1IdpIdentityprovidersListTimeRangeErrorComponent |
            ApiV1IdpIdentityprovidersListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1IdpIdentityprovidersListCreatedByUsersErrorComponent
        | ApiV1IdpIdentityprovidersListKindErrorComponent
        | ApiV1IdpIdentityprovidersListNameExactErrorComponent
        | ApiV1IdpIdentityprovidersListOrganizationsErrorComponent
        | ApiV1IdpIdentityprovidersListSearchErrorComponent
        | ApiV1IdpIdentityprovidersListStateErrorComponent
        | ApiV1IdpIdentityprovidersListStateNotErrorComponent
        | ApiV1IdpIdentityprovidersListSyncModeErrorComponent
        | ApiV1IdpIdentityprovidersListTimeRangeErrorComponent
        | ApiV1IdpIdentityprovidersListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_idp_identityproviders_list_created_by_users_error_component import (
            ApiV1IdpIdentityprovidersListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_kind_error_component import (
            ApiV1IdpIdentityprovidersListKindErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_name_exact_error_component import (
            ApiV1IdpIdentityprovidersListNameExactErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_organizations_error_component import (
            ApiV1IdpIdentityprovidersListOrganizationsErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_search_error_component import (
            ApiV1IdpIdentityprovidersListSearchErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_state_error_component import (
            ApiV1IdpIdentityprovidersListStateErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_state_not_error_component import (
            ApiV1IdpIdentityprovidersListStateNotErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_time_range_error_component import (
            ApiV1IdpIdentityprovidersListTimeRangeErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_workspaces_error_component import (
            ApiV1IdpIdentityprovidersListWorkspacesErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1IdpIdentityprovidersListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersListStateNotErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersListNameExactErrorComponent):
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
        from ..models.api_v1_idp_identityproviders_list_created_by_users_error_component import (
            ApiV1IdpIdentityprovidersListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_kind_error_component import (
            ApiV1IdpIdentityprovidersListKindErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_name_exact_error_component import (
            ApiV1IdpIdentityprovidersListNameExactErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_organizations_error_component import (
            ApiV1IdpIdentityprovidersListOrganizationsErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_search_error_component import (
            ApiV1IdpIdentityprovidersListSearchErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_state_error_component import (
            ApiV1IdpIdentityprovidersListStateErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_state_not_error_component import (
            ApiV1IdpIdentityprovidersListStateNotErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_sync_mode_error_component import (
            ApiV1IdpIdentityprovidersListSyncModeErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_time_range_error_component import (
            ApiV1IdpIdentityprovidersListTimeRangeErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_list_workspaces_error_component import (
            ApiV1IdpIdentityprovidersListWorkspacesErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1IdpIdentityprovidersListCreatedByUsersErrorComponent
                | ApiV1IdpIdentityprovidersListKindErrorComponent
                | ApiV1IdpIdentityprovidersListNameExactErrorComponent
                | ApiV1IdpIdentityprovidersListOrganizationsErrorComponent
                | ApiV1IdpIdentityprovidersListSearchErrorComponent
                | ApiV1IdpIdentityprovidersListStateErrorComponent
                | ApiV1IdpIdentityprovidersListStateNotErrorComponent
                | ApiV1IdpIdentityprovidersListSyncModeErrorComponent
                | ApiV1IdpIdentityprovidersListTimeRangeErrorComponent
                | ApiV1IdpIdentityprovidersListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_list_error_type_0 = (
                        ApiV1IdpIdentityprovidersListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_list_error_type_1 = (
                        ApiV1IdpIdentityprovidersListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_list_error_type_2 = (
                        ApiV1IdpIdentityprovidersListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_list_error_type_3 = (
                        ApiV1IdpIdentityprovidersListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_list_error_type_4 = (
                        ApiV1IdpIdentityprovidersListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_list_error_type_5 = (
                        ApiV1IdpIdentityprovidersListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_list_error_type_6 = (
                        ApiV1IdpIdentityprovidersListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_list_error_type_7 = (
                        ApiV1IdpIdentityprovidersListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_list_error_type_8 = (
                        ApiV1IdpIdentityprovidersListNameExactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_idp_identityproviders_list_error_type_9 = (
                    ApiV1IdpIdentityprovidersListSyncModeErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_idp_identityproviders_list_error_type_9

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_idp_identityproviders_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_idp_identityproviders_list_validation_error.additional_properties = d
        return api_v1_idp_identityproviders_list_validation_error

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
