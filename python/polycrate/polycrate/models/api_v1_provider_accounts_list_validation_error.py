from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_provider_accounts_list_api_kind_error_component import (
        ApiV1ProviderAccountsListApiKindErrorComponent,
    )
    from ..models.api_v1_provider_accounts_list_created_at_error_component import (
        ApiV1ProviderAccountsListCreatedAtErrorComponent,
    )
    from ..models.api_v1_provider_accounts_list_created_by_component_error_component import (
        ApiV1ProviderAccountsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_provider_accounts_list_created_by_users_error_component import (
        ApiV1ProviderAccountsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_provider_accounts_list_kind_error_component import ApiV1ProviderAccountsListKindErrorComponent
    from ..models.api_v1_provider_accounts_list_name_error_component import ApiV1ProviderAccountsListNameErrorComponent
    from ..models.api_v1_provider_accounts_list_name_exact_error_component import (
        ApiV1ProviderAccountsListNameExactErrorComponent,
    )
    from ..models.api_v1_provider_accounts_list_organization_error_component import (
        ApiV1ProviderAccountsListOrganizationErrorComponent,
    )
    from ..models.api_v1_provider_accounts_list_organizations_error_component import (
        ApiV1ProviderAccountsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_list_provider_entity_error_component import (
        ApiV1ProviderAccountsListProviderEntityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_list_scope_error_component import (
        ApiV1ProviderAccountsListScopeErrorComponent,
    )
    from ..models.api_v1_provider_accounts_list_search_error_component import (
        ApiV1ProviderAccountsListSearchErrorComponent,
    )
    from ..models.api_v1_provider_accounts_list_state_error_component import (
        ApiV1ProviderAccountsListStateErrorComponent,
    )
    from ..models.api_v1_provider_accounts_list_state_not_error_component import (
        ApiV1ProviderAccountsListStateNotErrorComponent,
    )
    from ..models.api_v1_provider_accounts_list_time_range_error_component import (
        ApiV1ProviderAccountsListTimeRangeErrorComponent,
    )
    from ..models.api_v1_provider_accounts_list_updated_at_error_component import (
        ApiV1ProviderAccountsListUpdatedAtErrorComponent,
    )
    from ..models.api_v1_provider_accounts_list_workspace_error_component import (
        ApiV1ProviderAccountsListWorkspaceErrorComponent,
    )
    from ..models.api_v1_provider_accounts_list_workspaces_error_component import (
        ApiV1ProviderAccountsListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ProviderAccountsListValidationError")


@_attrs_define
class ApiV1ProviderAccountsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ProviderAccountsListApiKindErrorComponent | ApiV1ProviderAccountsListCreatedAtErrorComponent |
            ApiV1ProviderAccountsListCreatedByComponentErrorComponent |
            ApiV1ProviderAccountsListCreatedByUsersErrorComponent | ApiV1ProviderAccountsListKindErrorComponent |
            ApiV1ProviderAccountsListNameErrorComponent | ApiV1ProviderAccountsListNameExactErrorComponent |
            ApiV1ProviderAccountsListOrganizationErrorComponent | ApiV1ProviderAccountsListOrganizationsErrorComponent |
            ApiV1ProviderAccountsListProviderEntityErrorComponent | ApiV1ProviderAccountsListScopeErrorComponent |
            ApiV1ProviderAccountsListSearchErrorComponent | ApiV1ProviderAccountsListStateErrorComponent |
            ApiV1ProviderAccountsListStateNotErrorComponent | ApiV1ProviderAccountsListTimeRangeErrorComponent |
            ApiV1ProviderAccountsListUpdatedAtErrorComponent | ApiV1ProviderAccountsListWorkspaceErrorComponent |
            ApiV1ProviderAccountsListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ProviderAccountsListApiKindErrorComponent
        | ApiV1ProviderAccountsListCreatedAtErrorComponent
        | ApiV1ProviderAccountsListCreatedByComponentErrorComponent
        | ApiV1ProviderAccountsListCreatedByUsersErrorComponent
        | ApiV1ProviderAccountsListKindErrorComponent
        | ApiV1ProviderAccountsListNameErrorComponent
        | ApiV1ProviderAccountsListNameExactErrorComponent
        | ApiV1ProviderAccountsListOrganizationErrorComponent
        | ApiV1ProviderAccountsListOrganizationsErrorComponent
        | ApiV1ProviderAccountsListProviderEntityErrorComponent
        | ApiV1ProviderAccountsListScopeErrorComponent
        | ApiV1ProviderAccountsListSearchErrorComponent
        | ApiV1ProviderAccountsListStateErrorComponent
        | ApiV1ProviderAccountsListStateNotErrorComponent
        | ApiV1ProviderAccountsListTimeRangeErrorComponent
        | ApiV1ProviderAccountsListUpdatedAtErrorComponent
        | ApiV1ProviderAccountsListWorkspaceErrorComponent
        | ApiV1ProviderAccountsListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_provider_accounts_list_api_kind_error_component import (
            ApiV1ProviderAccountsListApiKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_created_at_error_component import (
            ApiV1ProviderAccountsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_created_by_component_error_component import (
            ApiV1ProviderAccountsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_created_by_users_error_component import (
            ApiV1ProviderAccountsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_kind_error_component import (
            ApiV1ProviderAccountsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_name_error_component import (
            ApiV1ProviderAccountsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_organization_error_component import (
            ApiV1ProviderAccountsListOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_organizations_error_component import (
            ApiV1ProviderAccountsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_provider_entity_error_component import (
            ApiV1ProviderAccountsListProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_scope_error_component import (
            ApiV1ProviderAccountsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_search_error_component import (
            ApiV1ProviderAccountsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_state_error_component import (
            ApiV1ProviderAccountsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_state_not_error_component import (
            ApiV1ProviderAccountsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_time_range_error_component import (
            ApiV1ProviderAccountsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_updated_at_error_component import (
            ApiV1ProviderAccountsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_workspace_error_component import (
            ApiV1ProviderAccountsListWorkspaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_workspaces_error_component import (
            ApiV1ProviderAccountsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ProviderAccountsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsListApiKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsListOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsListWorkspaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsListProviderEntityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsListStateNotErrorComponent):
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
        from ..models.api_v1_provider_accounts_list_api_kind_error_component import (
            ApiV1ProviderAccountsListApiKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_created_at_error_component import (
            ApiV1ProviderAccountsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_created_by_component_error_component import (
            ApiV1ProviderAccountsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_created_by_users_error_component import (
            ApiV1ProviderAccountsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_kind_error_component import (
            ApiV1ProviderAccountsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_name_error_component import (
            ApiV1ProviderAccountsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_name_exact_error_component import (
            ApiV1ProviderAccountsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_organization_error_component import (
            ApiV1ProviderAccountsListOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_organizations_error_component import (
            ApiV1ProviderAccountsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_provider_entity_error_component import (
            ApiV1ProviderAccountsListProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_scope_error_component import (
            ApiV1ProviderAccountsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_search_error_component import (
            ApiV1ProviderAccountsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_state_error_component import (
            ApiV1ProviderAccountsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_state_not_error_component import (
            ApiV1ProviderAccountsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_time_range_error_component import (
            ApiV1ProviderAccountsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_updated_at_error_component import (
            ApiV1ProviderAccountsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_workspace_error_component import (
            ApiV1ProviderAccountsListWorkspaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_provider_accounts_list_workspaces_error_component import (
            ApiV1ProviderAccountsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ProviderAccountsListApiKindErrorComponent
                | ApiV1ProviderAccountsListCreatedAtErrorComponent
                | ApiV1ProviderAccountsListCreatedByComponentErrorComponent
                | ApiV1ProviderAccountsListCreatedByUsersErrorComponent
                | ApiV1ProviderAccountsListKindErrorComponent
                | ApiV1ProviderAccountsListNameErrorComponent
                | ApiV1ProviderAccountsListNameExactErrorComponent
                | ApiV1ProviderAccountsListOrganizationErrorComponent
                | ApiV1ProviderAccountsListOrganizationsErrorComponent
                | ApiV1ProviderAccountsListProviderEntityErrorComponent
                | ApiV1ProviderAccountsListScopeErrorComponent
                | ApiV1ProviderAccountsListSearchErrorComponent
                | ApiV1ProviderAccountsListStateErrorComponent
                | ApiV1ProviderAccountsListStateNotErrorComponent
                | ApiV1ProviderAccountsListTimeRangeErrorComponent
                | ApiV1ProviderAccountsListUpdatedAtErrorComponent
                | ApiV1ProviderAccountsListWorkspaceErrorComponent
                | ApiV1ProviderAccountsListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_0 = (
                        ApiV1ProviderAccountsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_1 = (
                        ApiV1ProviderAccountsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_2 = (
                        ApiV1ProviderAccountsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_3 = (
                        ApiV1ProviderAccountsListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_4 = (
                        ApiV1ProviderAccountsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_5 = (
                        ApiV1ProviderAccountsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_6 = (
                        ApiV1ProviderAccountsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_7 = (
                        ApiV1ProviderAccountsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_8 = (
                        ApiV1ProviderAccountsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_9 = (
                        ApiV1ProviderAccountsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_10 = (
                        ApiV1ProviderAccountsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_11 = (
                        ApiV1ProviderAccountsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_12 = (
                        ApiV1ProviderAccountsListApiKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_13 = (
                        ApiV1ProviderAccountsListOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_14 = (
                        ApiV1ProviderAccountsListWorkspaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_15 = (
                        ApiV1ProviderAccountsListProviderEntityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_list_error_type_16 = (
                        ApiV1ProviderAccountsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_list_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_provider_accounts_list_error_type_17 = (
                    ApiV1ProviderAccountsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_provider_accounts_list_error_type_17

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_provider_accounts_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_provider_accounts_list_validation_error.additional_properties = d
        return api_v1_provider_accounts_list_validation_error

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
