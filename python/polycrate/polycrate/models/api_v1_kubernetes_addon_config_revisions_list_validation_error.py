from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_addon_config_revisions_list_addon_error_component import (
        ApiV1KubernetesAddonConfigRevisionsListAddonErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_list_created_at_error_component import (
        ApiV1KubernetesAddonConfigRevisionsListCreatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_list_created_by_component_error_component import (
        ApiV1KubernetesAddonConfigRevisionsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_list_created_by_users_error_component import (
        ApiV1KubernetesAddonConfigRevisionsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_list_kind_error_component import (
        ApiV1KubernetesAddonConfigRevisionsListKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_list_name_error_component import (
        ApiV1KubernetesAddonConfigRevisionsListNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_list_name_exact_error_component import (
        ApiV1KubernetesAddonConfigRevisionsListNameExactErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_list_organizations_error_component import (
        ApiV1KubernetesAddonConfigRevisionsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_list_scope_error_component import (
        ApiV1KubernetesAddonConfigRevisionsListScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_list_search_error_component import (
        ApiV1KubernetesAddonConfigRevisionsListSearchErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_list_state_error_component import (
        ApiV1KubernetesAddonConfigRevisionsListStateErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_list_state_not_error_component import (
        ApiV1KubernetesAddonConfigRevisionsListStateNotErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_list_time_range_error_component import (
        ApiV1KubernetesAddonConfigRevisionsListTimeRangeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_list_updated_at_error_component import (
        ApiV1KubernetesAddonConfigRevisionsListUpdatedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_list_version_error_component import (
        ApiV1KubernetesAddonConfigRevisionsListVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_list_workspaces_error_component import (
        ApiV1KubernetesAddonConfigRevisionsListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAddonConfigRevisionsListValidationError")


@_attrs_define
class ApiV1KubernetesAddonConfigRevisionsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAddonConfigRevisionsListAddonErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsListCreatedAtErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsListCreatedByComponentErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsListCreatedByUsersErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsListKindErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsListNameErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsListNameExactErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsListOrganizationsErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsListScopeErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsListSearchErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsListStateErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsListStateNotErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsListTimeRangeErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsListUpdatedAtErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsListVersionErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAddonConfigRevisionsListAddonErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsListCreatedAtErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsListCreatedByComponentErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsListCreatedByUsersErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsListKindErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsListNameErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsListNameExactErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsListOrganizationsErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsListScopeErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsListSearchErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsListStateErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsListStateNotErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsListTimeRangeErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsListUpdatedAtErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsListVersionErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_addon_config_revisions_list_addon_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListAddonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_created_at_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_created_by_component_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_created_by_users_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_kind_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_organizations_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_scope_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_search_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_state_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_state_not_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_time_range_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_updated_at_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_version_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_workspaces_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsListAddonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsListVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsListStateNotErrorComponent):
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
        from ..models.api_v1_kubernetes_addon_config_revisions_list_addon_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListAddonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_created_at_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_created_by_component_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_created_by_users_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_kind_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_name_exact_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_organizations_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_scope_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_search_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_state_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_state_not_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_time_range_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_updated_at_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_version_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_list_workspaces_error_component import (
            ApiV1KubernetesAddonConfigRevisionsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAddonConfigRevisionsListAddonErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsListCreatedAtErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsListCreatedByComponentErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsListCreatedByUsersErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsListKindErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsListNameErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsListNameExactErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsListOrganizationsErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsListScopeErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsListSearchErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsListStateErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsListStateNotErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsListTimeRangeErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsListUpdatedAtErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsListVersionErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_0 = (
                        ApiV1KubernetesAddonConfigRevisionsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_1 = (
                        ApiV1KubernetesAddonConfigRevisionsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_2 = (
                        ApiV1KubernetesAddonConfigRevisionsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_3 = (
                        ApiV1KubernetesAddonConfigRevisionsListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_4 = (
                        ApiV1KubernetesAddonConfigRevisionsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_5 = (
                        ApiV1KubernetesAddonConfigRevisionsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_6 = (
                        ApiV1KubernetesAddonConfigRevisionsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_7 = (
                        ApiV1KubernetesAddonConfigRevisionsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_8 = (
                        ApiV1KubernetesAddonConfigRevisionsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_9 = (
                        ApiV1KubernetesAddonConfigRevisionsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_10 = (
                        ApiV1KubernetesAddonConfigRevisionsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_11 = (
                        ApiV1KubernetesAddonConfigRevisionsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_12 = (
                        ApiV1KubernetesAddonConfigRevisionsListAddonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_13 = (
                        ApiV1KubernetesAddonConfigRevisionsListVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_14 = (
                        ApiV1KubernetesAddonConfigRevisionsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_15 = (
                    ApiV1KubernetesAddonConfigRevisionsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_type_15

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_addon_config_revisions_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_addon_config_revisions_list_validation_error.additional_properties = d
        return api_v1_kubernetes_addon_config_revisions_list_validation_error

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
