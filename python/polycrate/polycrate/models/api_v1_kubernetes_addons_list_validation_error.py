from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_addons_list_block_name_error_component import (
        ApiV1KubernetesAddonsListBlockNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_list_catalogue_app_error_component import (
        ApiV1KubernetesAddonsListCatalogueAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_list_created_at_error_component import (
        ApiV1KubernetesAddonsListCreatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_list_created_by_component_error_component import (
        ApiV1KubernetesAddonsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_list_created_by_users_error_component import (
        ApiV1KubernetesAddonsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_list_enforcement_error_component import (
        ApiV1KubernetesAddonsListEnforcementErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_list_kind_error_component import ApiV1KubernetesAddonsListKindErrorComponent
    from ..models.api_v1_kubernetes_addons_list_name_error_component import ApiV1KubernetesAddonsListNameErrorComponent
    from ..models.api_v1_kubernetes_addons_list_name_exact_error_component import (
        ApiV1KubernetesAddonsListNameExactErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_list_organizations_error_component import (
        ApiV1KubernetesAddonsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_list_scope_error_component import (
        ApiV1KubernetesAddonsListScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_list_search_error_component import (
        ApiV1KubernetesAddonsListSearchErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_list_state_error_component import (
        ApiV1KubernetesAddonsListStateErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_list_state_not_error_component import (
        ApiV1KubernetesAddonsListStateNotErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_list_time_range_error_component import (
        ApiV1KubernetesAddonsListTimeRangeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_list_updated_at_error_component import (
        ApiV1KubernetesAddonsListUpdatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_list_workspaces_error_component import (
        ApiV1KubernetesAddonsListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAddonsListValidationError")


@_attrs_define
class ApiV1KubernetesAddonsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAddonsListBlockNameErrorComponent |
            ApiV1KubernetesAddonsListCatalogueAppErrorComponent | ApiV1KubernetesAddonsListCreatedAtErrorComponent |
            ApiV1KubernetesAddonsListCreatedByComponentErrorComponent |
            ApiV1KubernetesAddonsListCreatedByUsersErrorComponent | ApiV1KubernetesAddonsListEnforcementErrorComponent |
            ApiV1KubernetesAddonsListKindErrorComponent | ApiV1KubernetesAddonsListNameErrorComponent |
            ApiV1KubernetesAddonsListNameExactErrorComponent | ApiV1KubernetesAddonsListOrganizationsErrorComponent |
            ApiV1KubernetesAddonsListScopeErrorComponent | ApiV1KubernetesAddonsListSearchErrorComponent |
            ApiV1KubernetesAddonsListStateErrorComponent | ApiV1KubernetesAddonsListStateNotErrorComponent |
            ApiV1KubernetesAddonsListTimeRangeErrorComponent | ApiV1KubernetesAddonsListUpdatedAtErrorComponent |
            ApiV1KubernetesAddonsListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAddonsListBlockNameErrorComponent
        | ApiV1KubernetesAddonsListCatalogueAppErrorComponent
        | ApiV1KubernetesAddonsListCreatedAtErrorComponent
        | ApiV1KubernetesAddonsListCreatedByComponentErrorComponent
        | ApiV1KubernetesAddonsListCreatedByUsersErrorComponent
        | ApiV1KubernetesAddonsListEnforcementErrorComponent
        | ApiV1KubernetesAddonsListKindErrorComponent
        | ApiV1KubernetesAddonsListNameErrorComponent
        | ApiV1KubernetesAddonsListNameExactErrorComponent
        | ApiV1KubernetesAddonsListOrganizationsErrorComponent
        | ApiV1KubernetesAddonsListScopeErrorComponent
        | ApiV1KubernetesAddonsListSearchErrorComponent
        | ApiV1KubernetesAddonsListStateErrorComponent
        | ApiV1KubernetesAddonsListStateNotErrorComponent
        | ApiV1KubernetesAddonsListTimeRangeErrorComponent
        | ApiV1KubernetesAddonsListUpdatedAtErrorComponent
        | ApiV1KubernetesAddonsListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_addons_list_block_name_error_component import (
            ApiV1KubernetesAddonsListBlockNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_catalogue_app_error_component import (
            ApiV1KubernetesAddonsListCatalogueAppErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_created_at_error_component import (
            ApiV1KubernetesAddonsListCreatedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_created_by_component_error_component import (
            ApiV1KubernetesAddonsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_created_by_users_error_component import (
            ApiV1KubernetesAddonsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_enforcement_error_component import (
            ApiV1KubernetesAddonsListEnforcementErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_kind_error_component import (
            ApiV1KubernetesAddonsListKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_name_error_component import (
            ApiV1KubernetesAddonsListNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_organizations_error_component import (
            ApiV1KubernetesAddonsListOrganizationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_scope_error_component import (
            ApiV1KubernetesAddonsListScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_search_error_component import (
            ApiV1KubernetesAddonsListSearchErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_state_error_component import (
            ApiV1KubernetesAddonsListStateErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_state_not_error_component import (
            ApiV1KubernetesAddonsListStateNotErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_time_range_error_component import (
            ApiV1KubernetesAddonsListTimeRangeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_updated_at_error_component import (
            ApiV1KubernetesAddonsListUpdatedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_workspaces_error_component import (
            ApiV1KubernetesAddonsListWorkspacesErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAddonsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsListCatalogueAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsListEnforcementErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsListBlockNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsListStateNotErrorComponent):
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
        from ..models.api_v1_kubernetes_addons_list_block_name_error_component import (
            ApiV1KubernetesAddonsListBlockNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_catalogue_app_error_component import (
            ApiV1KubernetesAddonsListCatalogueAppErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_created_at_error_component import (
            ApiV1KubernetesAddonsListCreatedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_created_by_component_error_component import (
            ApiV1KubernetesAddonsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_created_by_users_error_component import (
            ApiV1KubernetesAddonsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_enforcement_error_component import (
            ApiV1KubernetesAddonsListEnforcementErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_kind_error_component import (
            ApiV1KubernetesAddonsListKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_name_error_component import (
            ApiV1KubernetesAddonsListNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_name_exact_error_component import (
            ApiV1KubernetesAddonsListNameExactErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_organizations_error_component import (
            ApiV1KubernetesAddonsListOrganizationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_scope_error_component import (
            ApiV1KubernetesAddonsListScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_search_error_component import (
            ApiV1KubernetesAddonsListSearchErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_state_error_component import (
            ApiV1KubernetesAddonsListStateErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_state_not_error_component import (
            ApiV1KubernetesAddonsListStateNotErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_time_range_error_component import (
            ApiV1KubernetesAddonsListTimeRangeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_updated_at_error_component import (
            ApiV1KubernetesAddonsListUpdatedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_list_workspaces_error_component import (
            ApiV1KubernetesAddonsListWorkspacesErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAddonsListBlockNameErrorComponent
                | ApiV1KubernetesAddonsListCatalogueAppErrorComponent
                | ApiV1KubernetesAddonsListCreatedAtErrorComponent
                | ApiV1KubernetesAddonsListCreatedByComponentErrorComponent
                | ApiV1KubernetesAddonsListCreatedByUsersErrorComponent
                | ApiV1KubernetesAddonsListEnforcementErrorComponent
                | ApiV1KubernetesAddonsListKindErrorComponent
                | ApiV1KubernetesAddonsListNameErrorComponent
                | ApiV1KubernetesAddonsListNameExactErrorComponent
                | ApiV1KubernetesAddonsListOrganizationsErrorComponent
                | ApiV1KubernetesAddonsListScopeErrorComponent
                | ApiV1KubernetesAddonsListSearchErrorComponent
                | ApiV1KubernetesAddonsListStateErrorComponent
                | ApiV1KubernetesAddonsListStateNotErrorComponent
                | ApiV1KubernetesAddonsListTimeRangeErrorComponent
                | ApiV1KubernetesAddonsListUpdatedAtErrorComponent
                | ApiV1KubernetesAddonsListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_list_error_type_0 = (
                        ApiV1KubernetesAddonsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_list_error_type_1 = (
                        ApiV1KubernetesAddonsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_list_error_type_2 = (
                        ApiV1KubernetesAddonsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_list_error_type_3 = (
                        ApiV1KubernetesAddonsListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_list_error_type_4 = (
                        ApiV1KubernetesAddonsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_list_error_type_5 = (
                        ApiV1KubernetesAddonsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_list_error_type_6 = (
                        ApiV1KubernetesAddonsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_list_error_type_7 = (
                        ApiV1KubernetesAddonsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_list_error_type_8 = (
                        ApiV1KubernetesAddonsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_list_error_type_9 = (
                        ApiV1KubernetesAddonsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_list_error_type_10 = (
                        ApiV1KubernetesAddonsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_list_error_type_11 = (
                        ApiV1KubernetesAddonsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_list_error_type_12 = (
                        ApiV1KubernetesAddonsListCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_list_error_type_13 = (
                        ApiV1KubernetesAddonsListEnforcementErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_list_error_type_14 = (
                        ApiV1KubernetesAddonsListBlockNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_list_error_type_15 = (
                        ApiV1KubernetesAddonsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_list_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_addons_list_error_type_16 = (
                    ApiV1KubernetesAddonsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_addons_list_error_type_16

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_addons_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_addons_list_validation_error.additional_properties = d
        return api_v1_kubernetes_addons_list_validation_error

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
