from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_registry_registries_list_created_by_users_error_component import (
        ApiV1RegistryRegistriesListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_registry_registries_list_kind_error_component import (
        ApiV1RegistryRegistriesListKindErrorComponent,
    )
    from ..models.api_v1_registry_registries_list_name_exact_error_component import (
        ApiV1RegistryRegistriesListNameExactErrorComponent,
    )
    from ..models.api_v1_registry_registries_list_organizations_error_component import (
        ApiV1RegistryRegistriesListOrganizationsErrorComponent,
    )
    from ..models.api_v1_registry_registries_list_search_error_component import (
        ApiV1RegistryRegistriesListSearchErrorComponent,
    )
    from ..models.api_v1_registry_registries_list_state_error_component import (
        ApiV1RegistryRegistriesListStateErrorComponent,
    )
    from ..models.api_v1_registry_registries_list_state_not_error_component import (
        ApiV1RegistryRegistriesListStateNotErrorComponent,
    )
    from ..models.api_v1_registry_registries_list_time_range_error_component import (
        ApiV1RegistryRegistriesListTimeRangeErrorComponent,
    )
    from ..models.api_v1_registry_registries_list_workspaces_error_component import (
        ApiV1RegistryRegistriesListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1RegistryRegistriesListValidationError")


@_attrs_define
class ApiV1RegistryRegistriesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1RegistryRegistriesListCreatedByUsersErrorComponent |
            ApiV1RegistryRegistriesListKindErrorComponent | ApiV1RegistryRegistriesListNameExactErrorComponent |
            ApiV1RegistryRegistriesListOrganizationsErrorComponent | ApiV1RegistryRegistriesListSearchErrorComponent |
            ApiV1RegistryRegistriesListStateErrorComponent | ApiV1RegistryRegistriesListStateNotErrorComponent |
            ApiV1RegistryRegistriesListTimeRangeErrorComponent | ApiV1RegistryRegistriesListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1RegistryRegistriesListCreatedByUsersErrorComponent
        | ApiV1RegistryRegistriesListKindErrorComponent
        | ApiV1RegistryRegistriesListNameExactErrorComponent
        | ApiV1RegistryRegistriesListOrganizationsErrorComponent
        | ApiV1RegistryRegistriesListSearchErrorComponent
        | ApiV1RegistryRegistriesListStateErrorComponent
        | ApiV1RegistryRegistriesListStateNotErrorComponent
        | ApiV1RegistryRegistriesListTimeRangeErrorComponent
        | ApiV1RegistryRegistriesListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_registry_registries_list_created_by_users_error_component import (
            ApiV1RegistryRegistriesListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_list_kind_error_component import (
            ApiV1RegistryRegistriesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_list_organizations_error_component import (
            ApiV1RegistryRegistriesListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_list_search_error_component import (
            ApiV1RegistryRegistriesListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_list_state_error_component import (
            ApiV1RegistryRegistriesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_list_state_not_error_component import (
            ApiV1RegistryRegistriesListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_list_time_range_error_component import (
            ApiV1RegistryRegistriesListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_list_workspaces_error_component import (
            ApiV1RegistryRegistriesListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1RegistryRegistriesListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesListStateNotErrorComponent):
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
        from ..models.api_v1_registry_registries_list_created_by_users_error_component import (
            ApiV1RegistryRegistriesListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_list_kind_error_component import (
            ApiV1RegistryRegistriesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_list_name_exact_error_component import (
            ApiV1RegistryRegistriesListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_list_organizations_error_component import (
            ApiV1RegistryRegistriesListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_list_search_error_component import (
            ApiV1RegistryRegistriesListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_list_state_error_component import (
            ApiV1RegistryRegistriesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_list_state_not_error_component import (
            ApiV1RegistryRegistriesListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_list_time_range_error_component import (
            ApiV1RegistryRegistriesListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_list_workspaces_error_component import (
            ApiV1RegistryRegistriesListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1RegistryRegistriesListCreatedByUsersErrorComponent
                | ApiV1RegistryRegistriesListKindErrorComponent
                | ApiV1RegistryRegistriesListNameExactErrorComponent
                | ApiV1RegistryRegistriesListOrganizationsErrorComponent
                | ApiV1RegistryRegistriesListSearchErrorComponent
                | ApiV1RegistryRegistriesListStateErrorComponent
                | ApiV1RegistryRegistriesListStateNotErrorComponent
                | ApiV1RegistryRegistriesListTimeRangeErrorComponent
                | ApiV1RegistryRegistriesListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_list_error_type_0 = (
                        ApiV1RegistryRegistriesListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_list_error_type_1 = (
                        ApiV1RegistryRegistriesListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_list_error_type_2 = (
                        ApiV1RegistryRegistriesListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_list_error_type_3 = (
                        ApiV1RegistryRegistriesListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_list_error_type_4 = (
                        ApiV1RegistryRegistriesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_list_error_type_5 = (
                        ApiV1RegistryRegistriesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_list_error_type_6 = (
                        ApiV1RegistryRegistriesListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_list_error_type_7 = (
                        ApiV1RegistryRegistriesListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_registry_registries_list_error_type_8 = (
                    ApiV1RegistryRegistriesListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_registry_registries_list_error_type_8

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_registry_registries_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_registry_registries_list_validation_error.additional_properties = d
        return api_v1_registry_registries_list_validation_error

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
